from __future__ import annotations

from pathlib import Path

from n8n_cost_analyzer.audit_pack import (
    _review_priority_label,
    generate_client_action_plan,
    generate_executive_summary,
)
from n8n_cost_analyzer.models import AnalysisResult, CostModel
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


def test_executive_summary_contains_score_interpretation():
    result = _build_result()
    md = generate_executive_summary(result)
    assert "How to Interpret Risk Scores" in md


def test_executive_summary_contains_how_to_read():
    result = _build_result()
    md = generate_executive_summary(result)
    assert "How to Read This Report" in md


def test_executive_summary_groups_ai_by_workflow():
    result = _build_result()
    md = generate_executive_summary(result)
    assert "AI/API nodes with variable token-based costs" in md


def test_executive_summary_no_workflows_pluralization():
    result = _build_result()
    md = generate_executive_summary(result)
    assert "workflow(s)" not in md


def test_client_action_plan_uses_highest_risk_workflows():
    result = _build_result()
    md = generate_client_action_plan(result)
    assert "Highest-Risk Workflows" in md


def test_client_action_plan_no_contradictory_however():
    result = _build_result()
    md = generate_client_action_plan(result)
    # Should NOT contain "No critical findings detected. However"
    assert "No critical findings detected. However" not in md


def test_client_action_plan_contains_how_to_read():
    result = _build_result()
    md = generate_client_action_plan(result)
    assert "How to Read This Plan" in md


def test_client_action_plan_compact_ai_format():
    result = _build_result()
    md = generate_client_action_plan(result)
    assert "Set usage limits and monitoring for AI/API nodes" in md
    assert "Highest AI exposure" in md


def test_client_action_plan_compact_error_handling():
    result = _build_result()
    md = generate_client_action_plan(result)
    assert "Configure error workflows for" in md


def test_client_action_plan_references_workflow_names():
    result = _build_result()
    md = generate_client_action_plan(result)
    assert "Polling Workflow" in md or "Loop HTTP Workflow" in md


def test_executive_summary_no_pluralization_artifacts():
    result = _build_result()
    md = generate_executive_summary(result)
    assert "finding(s)" not in md
    assert "node(s)" not in md


def test_executive_summary_uses_overall_portfolio_risk():
    result = _build_result()
    md = generate_executive_summary(result)
    assert "Overall portfolio risk" in md


def test_executive_summary_uses_operational_reliability():
    result = _build_result()
    md = generate_executive_summary(result)
    assert "Operational / reliability risk" in md


def test_executive_summary_no_overall_risk_level():
    result = _build_result()
    md = generate_executive_summary(result)
    assert "Overall risk level" not in md


def test_review_priority_label():
    assert _review_priority_label(95, True, 1) == "Critical"
    assert _review_priority_label(95, False, 0) == "Highest priority"
    assert _review_priority_label(75, False, 0) == "High priority"
    assert _review_priority_label(50, False, 0) == "Review recommended"
    assert _review_priority_label(30, False, 0) == "Moderate"
    assert _review_priority_label(10, False, 0) == "Low"


# === New v0.9 section tests ===

def test_executive_summary_contains_portfolio_insights():
    result = _build_result()
    md = generate_executive_summary(result)
    assert "## Portfolio Insights" in md
    assert "**Interpretation:**" in md


def test_executive_summary_contains_top_risk_patterns():
    result = _build_result()
    md = generate_executive_summary(result)
    assert "## Top Risk Patterns Detected" in md
    assert "AI/API cost exposure" in md or "Missing error handling" in md


def test_executive_summary_contains_cost_exposure():
    result = _build_result()
    md = generate_executive_summary(result)
    assert "## Cost Exposure Overview" in md
    assert "cost uncertainty in the portfolio" in md


def test_executive_summary_contains_credential_footprint():
    result = _build_result()
    md = generate_executive_summary(result)
    assert "## Credential Footprint" in md
    assert "credential scoping" in md


def test_executive_summary_contains_what_to_do_first():
    result = _build_result()
    md = generate_executive_summary(result)
    assert "## What To Do First" in md


def test_executive_summary_top_workflows_has_concentration():
    result = _build_result()
    md = generate_executive_summary(result)
    assert "Concentration" in md
    assert "High" in md or "Medium" in md or "Low" in md


def test_executive_summary_top_workflows_table_exists():
    result = _build_result()
    md = generate_executive_summary(result)
    assert "## Top Workflows To Review" in md
    assert "| # | Workflow |" in md


def test_executive_summary_has_business_impact_subsections():
    result = _build_result()
    md = generate_executive_summary(result)
    assert "### Cost Risk" in md
    assert "### Reliability Risk" in md
    assert "### Operational Complexity" in md
    assert "### Governance" in md


def test_executive_summary_no_key_finds_legacy():
    """Old '## Key Findings' section header should not exist anymore."""
    result = _build_result()
    md = generate_executive_summary(result)
    assert "## Key Findings" not in md


def test_executive_summary_output_size_under_2x():
    """Output should not exceed 2x the baseline size (75 lines → 150 lines max)."""
    result = _build_result()
    md = generate_executive_summary(result)
    lines = md.strip().split("\n")
    assert len(lines) < 150, f"Executive summary too long: {len(lines)} lines"


def test_executive_summary_risk_patterns_show_cause_and_impact():
    result = _build_result()
    md = generate_executive_summary(result)
    assert "→ Caused by:" in md
    assert "→ Impact:" in md


# === v0.9.2 Conditional Wording Tests ===

def test_no_immediately_without_critical_findings():
    """When critical_findings == 0, 'immediately' should not appear in What To Do First."""
    result = _build_result()
    md = generate_executive_summary(result)
    assert "immediately" not in md


def test_immediately_with_critical_findings():
    """When critical_findings > 0, 'immediately' should appear in What To Do First."""
    from n8n_cost_analyzer.models import (
        AnalysisResult, ScoreSummary, WorkflowRiskReport, RiskFinding,
        WorkflowRankingEntry, NodeInventory,
    )
    finding = RiskFinding(
        rule_id="LOOP_HTTP", severity="critical", category="cost",
        message="test critical", recommendation="fix",
        workflow_name="Critical WF",
    )
    report = WorkflowRiskReport(
        workflow_name="Critical WF", workflow_id="1", active=True,
        node_count=1, trigger_types=(), findings=(finding,),
        overall_risk_score=100, cost_risk_score=90,
    )
    result = AnalysisResult(
        reports=(report,),
        score_summary=ScoreSummary(overall_risk_score=50, cost_risk_score=50),
        recommendations=(),
        workflow_rankings=(WorkflowRankingEntry(
            rank=1, workflow_name="Critical WF", overall_risk_score=100,
            cost_risk_score=90, finding_count=1, critical_count=1, high_count=0,
            top_risk_drivers=("LOOP_HTTP",),
        ),),
        node_inventory=NodeInventory(
            node_type_counts={}, node_category_counts={},
            credential_reference_count=0, trigger_node_count=0,
        ),
    )
    md = generate_executive_summary(result)
    assert "immediately" in md


def test_low_credential_density_not_widespread():
    """When cred_refs < workflow_count, should NOT say 'widespread'."""
    from n8n_cost_analyzer.models import (
        AnalysisResult, ScoreSummary, WorkflowRiskReport,
        NodeInventory, WorkflowRankingEntry,
    )
    report = WorkflowRiskReport(
        workflow_name="Test WF", workflow_id="1", active=True,
        node_count=1, trigger_types=(), findings=(),
    )
    result = AnalysisResult(
        reports=(report, report, report, report, report, report,
                 report, report, report, report, report, report),  # 12 workflows
        score_summary=ScoreSummary(),
        recommendations=(),
        workflow_rankings=(),
        node_inventory=NodeInventory(
            node_type_counts={}, node_category_counts={},
            credential_reference_count=2, trigger_node_count=0,
        ),
    )
    md = generate_executive_summary(result)
    assert "present but not widespread" in md
    assert "Credential usage is widespread" not in md


def test_high_credential_density_widespread():
    """When avg_cred >= 3, should say 'widespread'."""
    from n8n_cost_analyzer.models import (
        AnalysisResult, ScoreSummary, WorkflowRiskReport,
        NodeInventory, WorkflowRankingEntry,
    )
    report = WorkflowRiskReport(
        workflow_name="Test WF", workflow_id="1", active=True,
        node_count=1, trigger_types=(), findings=(),
    )
    # 10 workflows, 50 refs → avg 5.0, >= 3 → widespread
    result = AnalysisResult(
        reports=(report,) * 10,
        score_summary=ScoreSummary(),
        recommendations=(),
        workflow_rankings=(),
        node_inventory=NodeInventory(
            node_type_counts={}, node_category_counts={},
            credential_reference_count=50, trigger_node_count=0,
        ),
    )
    md = generate_executive_summary(result)
    assert "Credential usage is widespread" in md


def test_zero_credential_refs_wording():
    """When cred_refs == 0, should use 'No credential references detected.'"""
    from n8n_cost_analyzer.models import (
        AnalysisResult, ScoreSummary, WorkflowRiskReport,
        NodeInventory, WorkflowRankingEntry,
    )
    report = WorkflowRiskReport(
        workflow_name="Test WF", workflow_id="1", active=True,
        node_count=1, trigger_types=(), findings=(),
    )
    result = AnalysisResult(
        reports=(report,) * 10,
        score_summary=ScoreSummary(),
        recommendations=(),
        workflow_rankings=(),
        node_inventory=NodeInventory(
            node_type_counts={}, node_category_counts={},
            credential_reference_count=0, trigger_node_count=0,
        ),
    )
    md = generate_executive_summary(result)
    assert "No credential references detected" in md


def test_top_risk_patterns_no_bad_pluralization():
    """No '1 workflows', '1 occurrences', '1 nodes', '1 types' should appear."""
    result = _build_result()
    md = generate_executive_summary(result)
    assert "1 workflows" not in md
    assert "1 occurrences" not in md
    assert "1 nodes" not in md
    assert "1 types" not in md


def test_high_score_without_critical_is_highest_priority():
    """Score 100 with no critical finding → 'Highest priority', not 'Critical'."""
    assert _review_priority_label(100, False, 0) == "Highest priority"
    assert _review_priority_label(95, False, 0) == "Highest priority"
    assert _review_priority_label(90, False, 0) == "Highest priority"


def test_critical_priority_requires_critical_finding():
    """'Critical' priority requires critical_count > 0."""
    assert _review_priority_label(100, True, 1) == "Critical"
    assert _review_priority_label(95, True, 1) == "Critical"
    assert _review_priority_label(100, True, 0) == "Highest priority"  # has critical elsewhere, not here
