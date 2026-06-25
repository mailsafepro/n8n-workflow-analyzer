from __future__ import annotations

from pathlib import Path

from n8n_cost_analyzer.parser import parse_workflow_directory
from n8n_cost_analyzer.rules import analyze_workflows
from n8n_cost_analyzer.scoring import rank_workflows, score_analysis

FIXTURES = Path(__file__).parent / "fixtures"


def _build_result():
    workflows = parse_workflow_directory(FIXTURES)
    reports = analyze_workflows(workflows)
    result = score_analysis(reports)
    return result


def test_ranking_sorted_by_score_desc():
    result = _build_result()
    rankings = rank_workflows(result)
    assert len(rankings) >= 1
    for i in range(len(rankings) - 1):
        assert rankings[i].overall_risk_score >= rankings[i + 1].overall_risk_score


def test_ranking_contains_expected_workflows():
    result = _build_result()
    rankings = rank_workflows(result)
    names = [e.workflow_name for e in rankings]
    assert "Simple Webhook Workflow" in names
    assert "Polling Workflow" in names


def test_ranking_has_unique_ranks():
    result = _build_result()
    rankings = rank_workflows(result)
    ranks = [e.rank for e in rankings]
    assert ranks == list(range(1, len(rankings) + 1))


def test_ranking_entry_fields():
    result = _build_result()
    rankings = rank_workflows(result)
    entry = rankings[0]
    assert entry.workflow_name
    assert entry.overall_risk_score >= 0
    assert entry.cost_risk_score >= 0
    assert entry.finding_count >= 0
    assert isinstance(entry.top_risk_drivers, tuple)


def test_high_score_workflows_ranked_first():
    result = _build_result()
    rankings = rank_workflows(result)
    # Loop HTTP should be highest risk among our fixtures
    assert rankings[0].overall_risk_score >= rankings[-1].overall_risk_score


def test_ranking_with_critical_findings_sort():
    from n8n_cost_analyzer.models import RiskFinding, ScoreSummary, WorkflowRiskReport

    # Create two workflows: one with critical finding, one without
    report_a = WorkflowRiskReport(
        workflow_name="A",
        workflow_id=None,
        active=True,
        node_count=2,
        trigger_types=(),
        findings=(
            RiskFinding(
                rule_id="CRIT", severity="critical", category="cost",
                message="c", recommendation="fix",
                workflow_name="A",
            ),
        ),
        overall_risk_score=50,
        cost_risk_score=50,
    )
    report_b = WorkflowRiskReport(
        workflow_name="B",
        workflow_id=None,
        active=True,
        node_count=2,
        trigger_types=(),
        findings=(
            RiskFinding(
                rule_id="HIGH", severity="high", category="cost",
                message="h", recommendation="fix",
                workflow_name="B",
            ),
        ),
        overall_risk_score=30,
        cost_risk_score=30,
    )
    from n8n_cost_analyzer.models import AnalysisResult
    result = AnalysisResult(
        reports=(report_a, report_b),
        score_summary=ScoreSummary(),
    )
    rankings = rank_workflows(result)
    assert rankings[0].workflow_name == "A"
    assert rankings[1].workflow_name == "B"
