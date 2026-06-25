from __future__ import annotations

import sys
from pathlib import Path

from n8n_cost_analyzer.audit_pack import write_audit_pack
from n8n_cost_analyzer.cost_model import load_cost_model
from n8n_cost_analyzer.json_report import write_json_report
from n8n_cost_analyzer.parser import parse_workflow_collection, parse_workflow_directory
from n8n_cost_analyzer.recommendations import generate_recommendations
from n8n_cost_analyzer.report import generate_markdown_report, write_markdown_report
from n8n_cost_analyzer.rules import analyze_workflows
from n8n_cost_analyzer.scoring import (
    compute_connection_inventory,
    compute_node_inventory,
    compute_workflows_extra,
    estimate_workflow_costs,
    rank_workflows,
    score_analysis,
)


def _parse_input(path: str | Path):
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"path does not exist: {p}")
    if p.is_dir():
        return parse_workflow_directory(p)
    if p.suffix.lower() == ".json":
        return parse_workflow_collection(p)
    raise ValueError(f"unsupported path (must be .json file or directory): {p}")


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    if not argv or argv[0] in ("-h", "--help"):
        print(
            "Usage: python -m n8n_cost_analyzer.cli analyze <path> "
            "[--output <file>] [--output-json <file>] [--cost-model <file>] "
            "[--audit-pack <dir>] [--fail-on-critical] [--include-disabled]",
            file=sys.stderr,
        )
        return 0 if argv and argv[0] in ("-h", "--help") else 1

    command = argv[0]
    if command != "analyze":
        print(f"Error: unknown command '{command}'. Use 'analyze'", file=sys.stderr)
        return 1

    args = argv[1:]
    input_path: str | None = None
    output_path: str | None = None
    output_json_path: str | None = None
    cost_model_path: str | None = None
    audit_pack_dir: str | None = None
    fail_on_critical = False
    include_disabled = False

    i = 0
    while i < len(args):
        if args[i] == "--output" and i + 1 < len(args):
            output_path = args[i + 1]
            i += 2
        elif args[i] == "--output-json" and i + 1 < len(args):
            output_json_path = args[i + 1]
            i += 2
        elif args[i] == "--cost-model" and i + 1 < len(args):
            cost_model_path = args[i + 1]
            i += 2
        elif args[i] == "--audit-pack" and i + 1 < len(args):
            audit_pack_dir = args[i + 1]
            i += 2
        elif args[i] == "--fail-on-critical":
            fail_on_critical = True
            i += 1
        elif args[i] == "--include-disabled":
            include_disabled = True
            i += 1
        elif args[i].startswith("--"):
            print(f"Error: unknown flag {args[i]}", file=sys.stderr)
            return 1
        else:
            input_path = args[i]
            i += 1

    if not input_path:
        print("Error: no input path provided", file=sys.stderr)
        return 1

    try:
        workflows = _parse_input(input_path)
    except (FileNotFoundError, NotADirectoryError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    if not workflows:
        print("Error: no valid workflows found", file=sys.stderr)
        return 1

    try:
        cost_model = load_cost_model(cost_model_path)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    reports = analyze_workflows(workflows, include_disabled=include_disabled)
    result = score_analysis(reports)
    all_findings = [f for r in result.reports for f in r.findings]
    recs = generate_recommendations(all_findings)
    rankings = rank_workflows(result)
    cost_estimates = estimate_workflow_costs(result, cost_model)
    node_inventory = compute_node_inventory(reports, workflows)
    connection_inventory = compute_connection_inventory(reports, workflows)
    workflows_extra = compute_workflows_extra(workflows)

    # Collect parser warnings from all workflows
    parser_warnings: list[str] = []
    for wf in workflows:
        parser_warnings.extend(wf.parser_warnings)

    result = type(result)(
        reports=result.reports,
        score_summary=result.score_summary,
        recommendations=recs,
        cost_model=cost_model,
        cost_estimates=cost_estimates,
        workflow_rankings=rankings,
        node_inventory=node_inventory,
        connection_inventory=connection_inventory,
        parser_warnings=tuple(parser_warnings),
        workflows_extra=workflows_extra,
    )

    s = result.score_summary
    print("n8n Cost Analyzer — Summary")
    print(f"  Workflows: {len(result.reports)}")
    print(f"  Overall risk: {s.overall_risk_score}/100")
    print(f"  Cost risk: {s.cost_risk_score}/100")
    print(f"  Operational risk: {s.operational_risk_score}/100")
    print(f"  Complexity: {s.complexity_score}/100")
    print(f"  Findings: {len(all_findings)}")
    if rankings:
        print(f"  Top workflow to review: {rankings[0].workflow_name}")
    if parser_warnings:
        print(f"  Parser warnings: {len(parser_warnings)}")
    if node_inventory and node_inventory.unknown_node_types:
        print(f"  Unknown node types: {len(node_inventory.unknown_node_types)}")
    if node_inventory and node_inventory.disabled_node_count > 0 and not include_disabled:
        print(f"  Disabled nodes skipped: {node_inventory.disabled_node_count} (use --include-disabled to analyze)")
    has_critical = any(f.severity == "critical" for f in all_findings)
    if has_critical:
        print("  ⚠ Critical findings detected!")

    if output_path:
        write_markdown_report(result, output_path, cost_model)
        print(f"  Report written to: {output_path}")
    else:
        print(generate_markdown_report(result, cost_model))

    if output_json_path:
        write_json_report(result, output_json_path, cost_model)
        print(f"  JSON report written to: {output_json_path}")

    if audit_pack_dir:
        write_audit_pack(result, audit_pack_dir, cost_model)
        print(f"  Audit pack written to: {audit_pack_dir}")

    if fail_on_critical and has_critical:
        return 2

    return 0


if __name__ == "__main__":
    sys.exit(main())
