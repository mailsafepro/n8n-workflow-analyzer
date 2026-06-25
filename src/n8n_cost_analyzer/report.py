from __future__ import annotations

from pathlib import Path

from n8n_cost_analyzer.models import AnalysisResult, CostModel, WorkflowRiskReport
from n8n_cost_analyzer.text_helpers import pluralize
from n8n_cost_analyzer.version import __version__


def _should_truncate(result: AnalysisResult) -> bool:
    """Returns True when report should be truncated for large corpora."""
    if len(result.reports) > 30:
        return True
    all_findings = [f for r in result.reports for f in r.findings]
    if len(all_findings) > 100:
        return True
    return False


def _maybe_truncate(items: list, max_rows: int) -> tuple[list, int]:
    """If items exceed max_rows, return (truncated, remaining_count)."""
    if len(items) > max_rows:
        return items[:max_rows], len(items) - max_rows
    return items, 0


def _remaining_note(remaining: int, label: str) -> str:
    if remaining > 0:
        return f"*... and {remaining} more {label} (table truncated for readability)*"
    return ""


def _score_bar(score: int) -> str:
    filled = score // 10
    empty = 10 - filled
    return "█" * filled + "░" * empty


def _severity_label(score: int) -> str:
    if score >= 70:
        return "🔴 Critical"
    if score >= 40:
        return "🟡 High"
    if score >= 20:
        return "🟠 Medium"
    if score > 0:
        return "🟢 Low"
    return "⚪ None"


def _severity_icon(severity: str) -> str:
    return {"critical": "🔴", "high": "🟡", "medium": "🟠", "low": "🟢"}.get(severity, "⚪")


def _risk_label(score: int) -> str:
    if score >= 70:
        return "high"
    if score >= 40:
        return "medium"
    if score > 0:
        return "low"
    return "none"


def _priority_label(score: int) -> str:
    if score >= 90:
        return "Highest priority"
    if score >= 70:
        return "High priority"
    if score >= 40:
        return "Review recommended"
    if score >= 20:
        return "Moderate"
    return "Low"


def _workflow_narrative(rpt: WorkflowRiskReport) -> str:
    parts: list[str] = []
    rule_ids = {f.rule_id for f in rpt.findings}
    ai_count = sum(1 for f in rpt.findings if f.rule_id == "AI_NODE")

    if "LOOP_HTTP" in rule_ids:
        parts.append("combines HTTP calls inside loop or batch logic, creating a runaway execution risk")
    if ai_count >= 3:
        parts.append(f"has {ai_count} AI/LLM nodes with variable token-based costs")
    elif ai_count > 0:
        parts.append("has AI/LLM nodes with variable token-based costs")
    if "FREQ_POLL" in rule_ids:
        parts.append("uses frequent polling which can drive high execution volume")
    if "NO_ERROR_HANDLING" in rule_ids:
        parts.append("lacks error handling for failure scenarios")
    if "HIGH_FAN_OUT" in rule_ids:
        parts.append("has a high fan-out node that may cause unexpected API load")
    if "MANY_HTTP" in rule_ids:
        for f in rpt.findings:
            if f.rule_id == "MANY_HTTP":
                parts.append("makes many external HTTP calls")
                break
    if "LARGE_WF" in rule_ids:
        parts.append("is a large workflow that is harder to maintain and debug")
    if "DB_IN_LOOP" in rule_ids:
        parts.append("runs database operations inside loops, risking performance issues")
    if "WEBHOOK_CHAIN" in rule_ids:
        parts.append("chains webhook triggers which can cascade unexpectedly")

    if not parts:
        level = _risk_label(rpt.overall_risk_score)
        if level == "none":
            return "No significant risks detected."
        if level == "low":
            return "Low risk. Maintain current practices."
        return "Review recommended."

    narrative = "; ".join(parts) + "."
    return narrative[0].upper() + narrative[1:]


def _workflow_next_action(rpt: WorkflowRiskReport, level: str) -> str:
    rule_ids = {f.rule_id for f in rpt.findings}
    if rpt.overall_risk_score >= 40:
        if "LOOP_HTTP" in rule_ids:
            return "Add rate limits and concurrency controls"
        if "AI_NODE" in rule_ids or "FREQ_POLL" in rule_ids:
            return "Estimate and monitor costs before production"
    if "NO_ERROR_HANDLING" in rule_ids:
        return "Configure error workflow"
    if "HIGH_FAN_OUT" in rule_ids:
        return "Review branching logic and reduce fan-out"
    return "Review and assess"


def generate_markdown_report(
    result: AnalysisResult,
    cost_model: CostModel | None = None,
) -> str:
    lines: list[str] = []
    s = result.score_summary
    all_findings = [f for r in result.reports for f in r.findings]
    total_critical = sum(1 for f in all_findings if f.severity == "critical")
    total_high = sum(1 for f in all_findings if f.severity == "high")
    top_category = _top_risk_category(all_findings)
    most_urgent = ""
    if result.workflow_rankings:
        most_urgent = result.workflow_rankings[0].workflow_name
    ni = result.node_inventory

    lines.append("# n8n Workflow Cost & Risk Report")
    lines.append("")

    # How to read this report
    lines.append("## How to Read This Report")
    lines.append("")
    lines.append("If you only have a few minutes, start with these sections:")
    lines.append("")
    lines.append("1. **Audit Summary** — overall risk scores at a glance")
    lines.append("2. **Top Workflows To Review First** — ranked by risk")
    lines.append("3. **Workflow Summaries** — one-line narrative per workflow")
    lines.append("4. **Quick Wins** — immediate actions with the most impact")
    lines.append("")
    lines.append("For a deeper review, read the full report in order.")
    lines.append("")

    # Audit Summary
    lines.append("## Audit Summary")
    lines.append("")
    lines.append(f"- **Overall Risk Score:** {s.overall_risk_score}/100 {_score_bar(s.overall_risk_score)}")
    lines.append(f"- **Risk Level:** {_severity_label(s.overall_risk_score)}")
    lines.append(f"- **Workflows analyzed:** {pluralize(len(result.reports), 'workflow')}")
    high_risk_count = sum(1 for r in result.reports if r.overall_risk_score >= 40)
    if high_risk_count > 0:
        lines.append(f"- **High-risk workflows:** {high_risk_count}")
    lines.append(
        f"- **Total findings:** {pluralize(len(all_findings), 'finding')} "
        f"({pluralize(total_critical, 'critical')}, {pluralize(total_high, 'high')})"
    )
    lines.append(f"- **Top risk category:** {top_category}")
    lines.append(f"- **Most urgent workflow:** {most_urgent or '—'}")
    if result.parser_warnings:
        lines.append(f"- **Parser warnings:** {pluralize(len(result.parser_warnings), 'warning')}")
    lines.append("")

    # Parser Warnings
    if result.parser_warnings:
        lines.append("## Parser Warnings")
        lines.append("")
        for w in result.parser_warnings:
            lines.append(f"- ⚠ {w}")
        lines.append("")

    # Executive Summary
    lines.append("## Executive Summary")
    lines.append("")
    lines.append(f"- **Cost Risk Score:** {s.cost_risk_score}/100 {_score_bar(s.cost_risk_score)}")
    lines.append(f"- **Operational Risk Score:** {s.operational_risk_score}/100 {_score_bar(s.operational_risk_score)}")
    lines.append(f"- **Complexity Score:** {s.complexity_score}/100 {_score_bar(s.complexity_score)}")
    if ni and ni.unknown_node_types:
        lines.append("")
        n_types = len(ni.unknown_node_types)
        lines.append(f"> **Note:** {pluralize(n_types, 'community/custom node type')} found. These may have cost or")
        lines.append("> risk profiles not covered by built-in rules. See the Community/Custom section for details.")
    lines.append("")

    # How to Interpret Risk Scores
    lines.append("## How to Interpret Risk Scores")
    lines.append("")
    lines.append("Risk scores are a relative indicator, not an absolute measure:")
    lines.append("")
    lines.append("| Range | Meaning |")
    lines.append("|-------|---------|")
    lines.append("| 0 | No risks detected |")
    lines.append("| 1–20 | Low risk — maintain current practices |")
    lines.append("| 21–40 | Moderate risk — monitor and plan mitigation |")
    lines.append("| 41–70 | Review recommended — address in the next cycle |")
    lines.append("| 71–100 | High priority — take immediate action |")
    lines.append("")
    lines.append("**Important:** The portfolio-level score (e.g., 12/100) can be low even if individual")
    lines.append("workflows have high scores. Always check the workflow rankings and per-workflow")
    lines.append("details to identify the most urgent items.")
    lines.append("")

    # Severity Legend
    lines.append("## Severity Legend")
    lines.append("")
    lines.append("| Severity | Meaning |")
    lines.append("|----------|---------|")
    lines.append("| CRITICAL | Immediate attention required. High probability of significant cost overruns or system failure. |")
    lines.append("| HIGH | Important risk that should be addressed in the next sprint/cycle. |")
    lines.append("| MEDIUM | Notable risk. Monitor and plan mitigation. |")
    lines.append("| LOW | Informational. Low probability of material impact. |")
    lines.append("")

    # Workflow Summaries
    lines.append("## Workflow Summaries")
    lines.append("")
    wf_reports, wf_remaining = _maybe_truncate(list(result.reports), 30)
    lines.append("| Workflow | Priority | Narrative | Next Action |")
    lines.append("|----------|----------|-----------|-------------|")
    for rpt in wf_reports:
        priority = _priority_label(rpt.overall_risk_score)
        narrative = _workflow_narrative(rpt)
        action = _workflow_next_action(rpt, priority)
        lines.append(
            f"| {rpt.workflow_name} | {priority} "
            f"({rpt.overall_risk_score}) | {narrative} | {action} |"
        )
    remaining_note = _remaining_note(wf_remaining, "workflows")
    if remaining_note:
        lines.append(remaining_note)
    lines.append("")

    if ni:
        lines.append("## Node Inventory")
        lines.append("")
        lines.append(f"- **Total unique node types:** {pluralize(len(ni.node_type_counts), 'type')}")
        lines.append(f"- **Trigger nodes:** {pluralize(ni.trigger_node_count, 'node')}")
        lines.append(f"- **Disabled nodes:** {pluralize(ni.disabled_node_count, 'node')}")
        lines.append(f"- **Credential references:** {pluralize(ni.credential_reference_count, 'reference')}")
        if ni.unknown_node_types:
            lines.append(f"- **Unknown node types:** {pluralize(len(ni.unknown_node_types), 'type')}")
        lines.append("")
        if ni.node_category_counts:
            lines.append("### Node Categories")
            lines.append("")
            lines.append("| Category | Count |")
            lines.append("|----------|-------|")
            for cat, count in sorted(ni.node_category_counts.items(), key=lambda x: -x[1]):
                lines.append(f"| {cat} | {count} |")
            lines.append("")
        if ni.node_type_counts:
            lines.append("### Node Types")
            lines.append("")
            lines.append("| Node Type | Count |")
            lines.append("|-----------|-------|")
            sorted_types = sorted(ni.node_type_counts.items(), key=lambda x: -x[1])
            node_types_list, nt_remaining = _maybe_truncate(sorted_types, 20)
            for ntype, count in node_types_list:
                lines.append(f"| {ntype} | {count} |")
            remaining_note = _remaining_note(nt_remaining, "node types")
            if remaining_note:
                lines.append(remaining_note)
        lines.append("")

    # Community / Custom / Unclassified Node Types
    if ni and ni.unknown_node_types:
        lines.append("## Community / Custom / Unclassified Node Types")
        lines.append("")
        n_unk = len(ni.unknown_node_types)
        verb = "is" if n_unk == 1 else "are"
        lines.append(f"The following {pluralize(n_unk, 'node type')} {verb} from community packages, custom builds,")
        lines.append("or unrecognized sources.")
        lines.append("They may have custom cost or risk profiles not covered by built-in rules:")
        lines.append("")
        unknown_list, unk_remaining = _maybe_truncate(list(ni.unknown_node_types), 20)
        for nt in unknown_list:
            lines.append(f"- `{nt}`")
        remaining_note = _remaining_note(unk_remaining, "unclassified node types")
        if remaining_note:
            lines.append(remaining_note)
        lines.append("")

    # Connection Inventory
    ci = result.connection_inventory
    if ci and ci.total_edges > 0:
        lines.append("## Connection Inventory")
        lines.append("")
        lines.append(f"- **Total edges:** {ci.total_edges}")
        lines.append(f"- **Max outgoing edges:** {ci.max_outgoing_edges}")
        if ci.high_fan_out_nodes:
            lines.append(f"- **High fan-out nodes:** {', '.join(ci.high_fan_out_nodes)}")
        if ci.isolated_node_names:
            lines.append(f"- **Isolated nodes:** {', '.join(ci.isolated_node_names)}")
        lines.append("")

    # Top Workflows To Review First
    lines.append("## Top Workflows To Review First")
    lines.append("")
    if result.workflow_rankings:
        lines.append("| Rank | Workflow | Overall Risk | Cost Risk | Critical | High | Top Drivers |")
        lines.append("|------|----------|-------------|-----------|----------|------|-------------|")
        for entry in result.workflow_rankings:
            drivers = ", ".join(entry.top_risk_drivers[:3]) if entry.top_risk_drivers else "—"
            lines.append(
                f"| {entry.rank} | {entry.workflow_name} | {entry.overall_risk_score} | "
                f"{entry.cost_risk_score} | {entry.critical_count} | {entry.high_count} | {drivers} |"
            )
    else:
        lines.append("No workflows to rank.")
    lines.append("")

    # Workflow Inventory
    lines.append("## Workflow Inventory")
    lines.append("")
    inv_reports, inv_remaining = _maybe_truncate(list(result.reports), 30)
    lines.append("| # | Workflow | Active | Nodes | Triggers | Risk Score |")
    lines.append("|---|----------|--------|-------|----------|------------|")
    for i, r in enumerate(inv_reports, 1):
        active_str = "✅" if r.active else "❌"
        triggers = ", ".join(r.trigger_types) if r.trigger_types else "none"
        lines.append(
            f"| {i} | {r.workflow_name} | {active_str} | {r.node_count} | {triggers} | {r.overall_risk_score} |"
        )
    remaining_note = _remaining_note(inv_remaining, "workflows")
    if remaining_note:
        lines.append(remaining_note)
    lines.append("")

    # Quick Wins
    lines.append("## Quick Wins")
    lines.append("")
    quick_wins = _build_specific_quick_wins(result)
    if quick_wins:
        for i, rec in enumerate(quick_wins[:5], 1):
            lines.append(f"{i}. {rec}")
    else:
        lines.append("No quick wins identified.")
    lines.append("")

    # Top Risks
    lines.append("## Top Risks")
    lines.append("")
    top = sorted(all_findings, key=lambda x: ("critical", "high", "medium", "low").index(x.severity))[:10]
    if top:
        lines.append("| Severity | Category | Workflow | Message |")
        lines.append("|----------|----------|----------|---------|")
        for f in top:
            lines.append(f"| {f.severity.upper()} | {f.category} | {f.workflow_name} | {f.message} |")
    else:
        lines.append("No risks found.")
    lines.append("")

    # Cost Risk Findings
    lines.append("## Cost Risk Findings")
    lines.append("")
    cost_findings = [f for f in all_findings if f.category == "cost"]
    if cost_findings:
        cf_list, cf_remaining = _maybe_truncate(cost_findings, 20)
        lines.append("| Severity | Workflow | Node(s) | Finding |")
        lines.append("|----------|----------|---------|---------|")
        for f in cf_list:
            nodes = ", ".join(f.node_names) if f.node_names else "—"
            lines.append(f"| {f.severity.upper()} | {f.workflow_name} | {nodes} | {f.message} |")
        remaining_note = _remaining_note(cf_remaining, "findings")
        if remaining_note:
            lines.append(remaining_note)
    else:
        lines.append("No cost-related findings.")
    lines.append("")

    # Estimated Cost Exposure
    lines.append("## Estimated Cost Exposure")
    lines.append("")
    if result.cost_estimates:
        for ce in result.cost_estimates:
            emoji = {"high": "🔴", "medium": "🟡", "low": "🟢", "unknown": "⚪"}
            icon = emoji.get(ce.estimated_cost_risk, "⚪")
            label = f"{icon} {ce.estimated_cost_risk.upper()} — {ce.estimated_monthly_exposure_label}"
            lines.append(f"- **{ce.workflow_name}:** {label}")
            if ce.risk_drivers:
                for d in ce.risk_drivers:
                    lines.append(f"  - Driver: {d}")
            if ce.notes:
                for n in ce.notes:
                    lines.append(f"  - Note: {n}")
    else:
        lines.append("No cost estimates available.")
    lines.append("")
    lines.append("*Cost estimates are heuristic — based on static analysis, not actual financial quotes.*")
    lines.append("")

    # Operational Risk Findings
    lines.append("## Operational Risk Findings")
    lines.append("")
    op_findings = [f for f in all_findings if f.category == "operational"]
    if op_findings:
        op_list, op_remaining = _maybe_truncate(op_findings, 20)
        lines.append("| Severity | Workflow | Node(s) | Finding |")
        lines.append("|----------|----------|---------|---------|")
        for f in op_list:
            nodes = ", ".join(f.node_names) if f.node_names else "—"
            lines.append(f"| {f.severity.upper()} | {f.workflow_name} | {nodes} | {f.message} |")
        remaining_note = _remaining_note(op_remaining, "findings")
        if remaining_note:
            lines.append(remaining_note)
    else:
        lines.append("No operational findings.")
    lines.append("")

    # Complexity Findings
    lines.append("## Complexity Findings")
    lines.append("")
    complexity_findings = [f for f in all_findings if f.category == "complexity"]
    if complexity_findings:
        cx_list, cx_remaining = _maybe_truncate(complexity_findings, 20)
        lines.append("| Severity | Workflow | Finding |")
        lines.append("|----------|----------|---------|")
        for f in cx_list:
            lines.append(f"| {f.severity.upper()} | {f.workflow_name} | {f.message} |")
        remaining_note = _remaining_note(cx_remaining, "findings")
        if remaining_note:
            lines.append(remaining_note)
    else:
        lines.append("No complexity findings.")
    lines.append("")

    # Recommendations
    lines.append("## Recommendations")
    lines.append("")
    if result.recommendations:
        for i, rec in enumerate(result.recommendations, 1):
            lines.append(f"{i}. {rec}")
    else:
        lines.append("No recommendations generated.")
    lines.append("")

    # Workflow-Level Details
    lines.append("## Workflow-Level Details")
    lines.append("")
    detail_reports, detail_remaining = _maybe_truncate(list(result.reports), 10)
    for rpt in detail_reports:
        lines.append(f"### {rpt.workflow_name}")
        lines.append("")
        lines.append(f"- **ID:** {rpt.workflow_id or 'N/A'}")
        lines.append(f"- **Active:** {'N/A' if rpt.active is None else ('✅' if rpt.active else '❌')}")
        lines.append(f"- **Nodes:** {rpt.node_count}")
        lines.append(f"- **Triggers:** {', '.join(rpt.trigger_types) if rpt.trigger_types else 'none'}")
        scores = f"Cost={rpt.cost_risk_score} | Ops={rpt.operational_risk_score}"
        scores += f" | Complexity={rpt.complexity_score} | Overall={rpt.overall_risk_score}"
        lines.append(f"- **Scores:** {scores}")
        if rpt.findings:
            lines.append("")
            lines.append("**Findings:**")
            for f in rpt.findings:
                lines.append(f"  - [{f.severity.upper()}] [{f.category}] {f.rule_id}: {f.message}")
                if f.node_names:
                    lines.append(f"    - Nodes: {', '.join(f.node_names)}")
        lines.append("")
    remaining_note = _remaining_note(detail_remaining, "workflows with hidden details")
    if remaining_note:
        lines.append(remaining_note)
        lines.append("")

    # Workflow Risk Ranking
    lines.append("## Workflow Risk Ranking")
    lines.append("")
    if result.workflow_rankings:
        lines.append("| Rank | Workflow | Overall | Cost | Ops | Complexity | Findings |")
        lines.append("|------|----------|---------|------|-----|------------|----------|")
        for entry in result.workflow_rankings:
            rpt = next((r for r in result.reports if r.workflow_name == entry.workflow_name), None)
            ops_score = rpt.operational_risk_score if rpt else 0
            complexity = rpt.complexity_score if rpt else 0
            lines.append(
                f"| {entry.rank} | {entry.workflow_name} | {entry.overall_risk_score} | "
                f"{entry.cost_risk_score} | {ops_score} | {complexity} | {entry.finding_count} |"
            )
    else:
        lines.append("No workflows to rank.")
    lines.append("")

    # Assumptions
    lines.append("## Assumptions")
    lines.append("")
    lines.append("- Analysis is based on exported JSON workflow definitions only.")
    lines.append("- Actual execution volume depends on trigger frequency and input data size.")
    lines.append("- AI/LLM costs are estimated based on node presence, not actual token usage.")
    lines.append("- HTTP call costs assume external API pricing not included.")
    lines.append("- Webhook chains are inferred from node types and URL patterns.")
    lines.append("- Cost estimates are heuristic and not financial quotes.")
    lines.append("- Credential references are counted; secrets are never exposed.")
    lines.append("- Disabled nodes are excluded from risk analysis by default.")
    lines.append("")

    # Appendix
    lines.append("## Appendix")
    lines.append("")
    lines.append("### Rule Reference")
    lines.append("")
    lines.append("| Rule ID | Description | Default Severity | Category |")
    lines.append("|---------|-------------|------------------|----------|")
    lines.append("| FREQ_POLL | Frequent polling/schedule trigger | high | cost |")
    lines.append("| LOOP_HTTP | Loop/batch combined with HTTP request | high | cost |")
    lines.append("| AI_NODE | AI/LLM node detected | medium | cost |")
    lines.append("| LARGE_WF | Workflow with many nodes | medium/critical | complexity |")
    lines.append("| NO_ERROR_HANDLING | Missing error workflow | medium | reliability |")
    lines.append("| WEBHOOK_CHAIN | Webhook chaining to internal URLs | medium/low | operational |")
    lines.append("| DB_IN_LOOP | Database operation inside loop | high | operational |")
    lines.append("| MANY_HTTP | Multiple HTTP Request nodes | low | cost |")
    lines.append("| HIGH_FAN_OUT | Node with 5+ outgoing connections | medium | complexity |")
    lines.append("")
    lines.append("---")
    lines.append(f"*Generated by n8n Cost Analyzer v{__version__}*")

    return "\n".join(lines)


def write_markdown_report(
    result: AnalysisResult,
    path: str | Path,
    cost_model: CostModel | None = None,
) -> Path:
    p = Path(path)
    content = generate_markdown_report(result, cost_model)
    p.write_text(content, encoding="utf-8")
    return p


def _build_specific_quick_wins(result: AnalysisResult) -> list[str]:
    wins: list[str] = []
    all_findings = [f for r in result.reports for f in r.findings]
    rule_ids = {f.rule_id for f in all_findings}

    # Workflow-specific LOOP_HTTP
    for rpt in result.reports:
        for f in rpt.findings:
            if f.rule_id == "LOOP_HTTP":
                wins.append(
                    f"Add rate limits and concurrency controls around the HTTP loop "
                    f"in '{rpt.workflow_name}'."
                )
                break

    # Per-workflow AI exposure
    ai_workflows = [(r, sum(1 for f in r.findings if f.rule_id == "AI_NODE")) for r in result.reports]
    high_ai = [(r, c) for r, c in ai_workflows if c >= 2]
    for rpt, count in high_ai:
        wins.append(
            f"Review AI cost exposure in '{rpt.workflow_name}' — "
            f"{pluralize(count, 'AI node')} with variable token-based costs."
        )

    # Error handling
    if "NO_ERROR_HANDLING" in rule_ids:
        no_handle_count = sum(1 for r in result.reports if any(f.rule_id == "NO_ERROR_HANDLING" for f in r.findings))
        wins.append(
            f"Configure error workflow handling in "
            f"{pluralize(no_handle_count, 'workflow')}."
        )

    # General wins from recommendations
    for rec in result.recommendations:
        # Only add recommendations not already covered by specific wins
        already_covered = any(w.lower().startswith(rec.split(".")[0][:20].lower()) for w in wins)
        if not already_covered:
            wins.append(rec)

    return wins


def _top_risk_category(findings_list: list) -> str:
    counts: dict[str, int] = {}
    for f in findings_list:
        cat: str = f.category
        counts[cat] = counts.get(cat, 0) + 1
    if not counts:
        return "none"
    return max(counts, key=lambda k: counts[k])  # type: ignore
