from __future__ import annotations

from pathlib import Path

from n8n_cost_analyzer.models import (
    AnalysisResult,
    CostModel,
    ScoreSummary,
)
from n8n_cost_analyzer.parser import parse_workflow_directory
from n8n_cost_analyzer.recommendations import generate_recommendations
from n8n_cost_analyzer.report import _priority_label, generate_markdown_report, write_markdown_report
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


def test_report_not_empty():
    result = _build_result()
    md = generate_markdown_report(result)
    assert len(md) > 100


def test_report_contains_workflow_names():
    result = _build_result()
    md = generate_markdown_report(result)
    assert "Simple Webhook Workflow" in md
    assert "Polling Workflow" in md


def test_report_contains_scores():
    result = _build_result()
    md = generate_markdown_report(result)
    assert "Overall Risk Score" in md
    assert "Cost Risk Score" in md
    assert "Operational Risk Score" in md
    assert "Complexity Score" in md


def test_report_contains_recommendations():
    result = _build_result()
    md = generate_markdown_report(result)
    assert "Recommendations" in md


def test_report_contains_rule_reference():
    result = _build_result()
    md = generate_markdown_report(result)
    assert "FREQ_POLL" in md
    assert "LOOP_HTTP" in md
    assert "AI_NODE" in md
    assert "HIGH_FAN_OUT" in md


def test_report_contains_executive_summary():
    result = _build_result()
    md = generate_markdown_report(result)
    assert "Executive Summary" in md


def test_report_contains_workflow_inventory():
    result = _build_result()
    md = generate_markdown_report(result)
    assert "Workflow Inventory" in md


def test_write_report_file(tmp_path: Path):
    result = _build_result()
    out = tmp_path / "report.md"
    write_markdown_report(result, out)
    assert out.exists()
    assert out.read_text().startswith("# n8n Workflow Cost & Risk Report")


def test_report_with_empty_workflows():
    result = AnalysisResult(
        reports=(),
        score_summary=ScoreSummary(),
        recommendations=(),
    )
    md = generate_markdown_report(result)
    assert "Executive Summary" in md
    assert "Workflow Inventory" in md


def test_report_shows_top_risks():
    result = _build_result()
    md = generate_markdown_report(result)
    assert "Top Risks" in md


def test_report_contains_audit_summary():
    result = _build_result()
    md = generate_markdown_report(result)
    assert "Audit Summary" in md


def test_report_contains_top_workflows_to_review():
    result = _build_result()
    md = generate_markdown_report(result)
    assert "Top Workflows To Review First" in md


def test_report_contains_severity_legend():
    result = _build_result()
    md = generate_markdown_report(result)
    assert "Severity Legend" in md


def test_report_contains_cost_exposure():
    result = _build_result()
    md = generate_markdown_report(result)
    assert "Estimated Cost Exposure" in md


def test_report_contains_quick_wins():
    result = _build_result()
    md = generate_markdown_report(result)
    assert "Quick Wins" in md


def test_report_contains_workflow_risk_ranking():
    result = _build_result()
    md = generate_markdown_report(result)
    assert "Workflow Risk Ranking" in md


def test_report_contains_node_inventory():
    result = _build_result()
    md = generate_markdown_report(result)
    assert "Node Inventory" in md


def test_report_contains_unknown_node_types():
    result = _build_result()
    md = generate_markdown_report(result)
    assert "Community / Custom / Unclassified Node Types" in md


def test_report_contains_node_categories():
    result = _build_result()
    md = generate_markdown_report(result)
    assert "Node Categories" in md
    assert "| Category | Count |" in md


def test_report_contains_connection_inventory():
    result = _build_result()
    md = generate_markdown_report(result)
    assert "Connection Inventory" in md


def test_no_credential_secrets_in_report():
    result = _build_result()
    md = generate_markdown_report(result)
    assert "sk-secret-123" not in md


def test_report_contains_how_to_read():
    result = _build_result()
    md = generate_markdown_report(result)
    assert "How to Read This Report" in md


def test_report_contains_risk_score_interpretation():
    result = _build_result()
    md = generate_markdown_report(result)
    assert "How to Interpret Risk Scores" in md


def test_report_contains_workflow_summaries():
    result = _build_result()
    md = generate_markdown_report(result)
    assert "Workflow Summaries" in md


def test_report_no_workflows_pluralization():
    result = _build_result()
    md = generate_markdown_report(result)
    assert "workflow(s)" not in md


def test_report_no_findings_pluralization():
    result = _build_result()
    md = generate_markdown_report(result)
    assert "finding(s)" not in md


def test_report_active_none_replaced():
    result = _build_result()
    md = generate_markdown_report(result)
    assert "**Active:** None" not in md


def test_report_pluralize_in_audit_summary():
    result = _build_result()
    md = generate_markdown_report(result)
    assert "1 workflow" in md or "workflows" in md


def test_report_uses_priority_column_in_summaries():
    result = _build_result()
    md = generate_markdown_report(result)
    assert "| Workflow | Priority |" in md


def test_report_uses_priority_labels():
    result = _build_result()
    md = generate_markdown_report(result)
    assert "Highest priority" in md or "High priority" in md or "Review recommended" in md or "Moderate" in md or "Low" in md


def test_report_no_risk_level_column():
    result = _build_result()
    md = generate_markdown_report(result)
    assert "| Risk Level |" not in md


def test_priority_label():
    assert _priority_label(95) == "Highest priority"
    assert _priority_label(75) == "High priority"
    assert _priority_label(50) == "Review recommended"
    assert _priority_label(30) == "Moderate"
    assert _priority_label(10) == "Low"


def test_should_truncate_small_corpus():
    from n8n_cost_analyzer.report import _should_truncate
    result = _build_result()
    assert not _should_truncate(result)


def test_should_truncate_large_workflow_count():
    from n8n_cost_analyzer.models import AnalysisResult, ScoreSummary, WorkflowRiskReport
    from n8n_cost_analyzer.report import _should_truncate
    reports = tuple(
        WorkflowRiskReport(workflow_name=f"wf{i}", workflow_id=str(i), active=True, node_count=1, findings=(), trigger_types=())
        for i in range(31)
    )
    result = AnalysisResult(reports=reports, score_summary=ScoreSummary(), recommendations=())
    assert _should_truncate(result)


def test_should_truncate_many_findings():
    from n8n_cost_analyzer.models import AnalysisResult, ScoreSummary, WorkflowRiskReport, RiskFinding
    from n8n_cost_analyzer.report import _should_truncate
    findings = tuple([
        RiskFinding(rule_id="AI_NODE", severity="medium", category="cost", message="x", recommendation="y",
                     workflow_name="wf", node_names=("n",))
        for _ in range(101)
    ])
    report = WorkflowRiskReport(workflow_name="wf", workflow_id="id", active=True, node_count=5, findings=findings, trigger_types=())
    result = AnalysisResult(
        reports=(report,),
        score_summary=ScoreSummary(),
        recommendations=(),
    )
    assert _should_truncate(result)


def test_maybe_truncate_noop_for_small_list():
    from n8n_cost_analyzer.report import _maybe_truncate
    items, remaining = _maybe_truncate([1, 2, 3], 5)
    assert items == [1, 2, 3]
    assert remaining == 0


def test_maybe_truncate_truncates_large_list():
    from n8n_cost_analyzer.report import _maybe_truncate
    items, remaining = _maybe_truncate(list(range(20)), 5)
    assert items == [0, 1, 2, 3, 4]
    assert remaining == 15


def test_remaining_note_empty():
    from n8n_cost_analyzer.report import _remaining_note
    assert _remaining_note(0, "workflows") == ""


def test_remaining_note_generates():
    from n8n_cost_analyzer.report import _remaining_note
    note = _remaining_note(7, "workflows")
    assert "... and 7 more workflows" in note
    assert "(table truncated" in note


def test_large_report_triggers_truncation_note():
    from n8n_cost_analyzer.models import (
        N8nNode, N8nWorkflow, AnalysisResult, ScoreSummary,
        WorkflowRiskReport, RiskFinding,
    )
    from n8n_cost_analyzer.report import _maybe_truncate, _should_truncate, generate_markdown_report
    from n8n_cost_analyzer.scoring import score_analysis

    # Build enough reports to trigger truncation
    reports_list = []
    for i in range(35):
        node = N8nNode(id=f"n{i}", name=f"N{i}", type="n8n-nodes-base.noOp", parameters={})
        wf = N8nWorkflow(id=f"wf{i}", name=f"WF{i}", active=True, nodes=(node,))
        from n8n_cost_analyzer.rules import analyze_workflow
        findings = analyze_workflow(wf)
        rpt = WorkflowRiskReport(
            workflow_name=wf.name, workflow_id=wf.id, active=True, node_count=1,
            findings=tuple(findings), trigger_types=(),
        )
        reports_list.append(rpt)

    result = score_analysis(reports_list)
    md = generate_markdown_report(result)
    # Should contain truncation note
    assert "... and 5 more workflows" in md


def test_truncation_sections_have_consistent_format():
    from n8n_cost_analyzer.models import (
        N8nNode, N8nWorkflow, AnalysisResult, ScoreSummary,
        WorkflowRiskReport, RiskFinding,
    )
    from n8n_cost_analyzer.report import generate_markdown_report
    from n8n_cost_analyzer.scoring import score_analysis

    reports_list = []
    for i in range(35):
        node = N8nNode(id=f"n{i}", name=f"N{i}", type="n8n-nodes-base.noOp", parameters={})
        wf = N8nWorkflow(id=f"wf{i}", name=f"WF{i}", active=True, nodes=(node,))
        from n8n_cost_analyzer.rules import analyze_workflow
        findings = analyze_workflow(wf)
        rpt = WorkflowRiskReport(
            workflow_name=wf.name, workflow_id=wf.id, active=True, node_count=1,
            findings=tuple(findings), trigger_types=(),
        )
        reports_list.append(rpt)

    result = score_analysis(reports_list)
    md = generate_markdown_report(result)
    # No italic markers should be broken
    assert "**" in md
    assert "(table truncated" in md
    assert "(table truncated for readability)" in md
