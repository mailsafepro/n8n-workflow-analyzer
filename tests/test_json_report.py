from __future__ import annotations

import json
from pathlib import Path

from n8n_cost_analyzer.json_report import generate_json_report, write_json_report
from n8n_cost_analyzer.models import AnalysisResult, CostModel, ScoreSummary
from n8n_cost_analyzer.parser import parse_workflow_directory
from n8n_cost_analyzer.recommendations import generate_recommendations
from n8n_cost_analyzer.rules import analyze_workflows
from n8n_cost_analyzer.scoring import (
    compute_connection_inventory,
    compute_node_inventory,
    compute_workflows_extra,
    estimate_workflow_costs,
    rank_workflows,
    score_analysis,
)
from n8n_cost_analyzer.version import __version__

FIXTURES = Path(__file__).parent / "fixtures"


def _build_result() -> AnalysisResult:
    workflows = parse_workflow_directory(FIXTURES)
    reports = analyze_workflows(workflows)
    result = score_analysis(reports)
    all_findings = [f for r in result.reports for f in r.findings]
    recs = generate_recommendations(all_findings)
    cm = CostModel()
    rankings = rank_workflows(result)
    estimates = estimate_workflow_costs(result, cm)
    ni = compute_node_inventory(reports, workflows)
    ci = compute_connection_inventory(reports, workflows)
    we = compute_workflows_extra(workflows)
    pw: list[str] = []
    for wf in workflows:
        pw.extend(wf.parser_warnings)
    return AnalysisResult(
        reports=result.reports,
        score_summary=result.score_summary,
        recommendations=recs,
        cost_model=cm,
        cost_estimates=estimates,
        workflow_rankings=rankings,
        node_inventory=ni,
        connection_inventory=ci,
        parser_warnings=tuple(pw),
        workflows_extra=we,
    )


def test_generate_returns_dict():
    result = _build_result()
    data = generate_json_report(result)
    assert isinstance(data, dict)


def test_contains_summary():
    result = _build_result()
    data = generate_json_report(result)
    assert "summary" in data
    s = data["summary"]
    assert s["workflow_count"] >= 1


def test_version_matches_version_module():
    result = _build_result()
    data = generate_json_report(result)
    assert data["version"] == __version__


def test_contains_workflow_rankings():
    result = _build_result()
    data = generate_json_report(result)
    assert "workflow_rankings" in data
    assert len(data["workflow_rankings"]) >= 1


def test_contains_findings():
    result = _build_result()
    data = generate_json_report(result)
    assert "findings" in data


def test_contains_recommendations():
    result = _build_result()
    data = generate_json_report(result)
    assert "recommendations" in data


def test_contains_cost_estimates():
    result = _build_result()
    data = generate_json_report(result)
    assert "cost_estimates" in data


def test_json_serializable():
    result = _build_result()
    data = generate_json_report(result)
    dumped = json.dumps(data, indent=2, ensure_ascii=False)
    assert len(dumped) > 50
    reloaded = json.loads(dumped)
    assert reloaded["summary"]["workflow_count"] == data["summary"]["workflow_count"]


def test_write_json_report(tmp_path: Path):
    result = _build_result()
    out = tmp_path / "report.json"
    write_json_report(result, out)
    assert out.exists()
    data = json.loads(out.read_text())
    assert "summary" in data


def test_empty_result():
    result = AnalysisResult(
        reports=(),
        score_summary=ScoreSummary(),
        recommendations=(),
        workflow_rankings=(),
        cost_estimates=(),
    )
    data = generate_json_report(result)
    assert data["summary"]["workflow_count"] == 0


def test_contains_node_inventory():
    result = _build_result()
    data = generate_json_report(result)
    assert "node_inventory" in data
    ni = data["node_inventory"]
    assert "node_type_counts" in ni
    assert "node_category_counts" in ni
    assert "unknown_node_types" in ni
    assert "disabled_node_count" in ni
    assert "credential_reference_count" in ni


def test_contains_connection_inventory():
    result = _build_result()
    data = generate_json_report(result)
    assert "connection_inventory" in data
    ci = data["connection_inventory"]
    assert "total_edges" in ci
    assert "high_fan_out_nodes" in ci


def test_contains_parser_warnings():
    result = _build_result()
    data = generate_json_report(result)
    assert "parser_warnings" in data


def test_contains_workflows_extra():
    result = _build_result()
    data = generate_json_report(result)
    assert "workflows_extra" in data
    assert len(data["workflows_extra"]) >= 1


def test_credentials_not_in_json_output():
    result = _build_result()
    data = json.dumps(generate_json_report(result))
    assert "sk-secret-123" not in data
