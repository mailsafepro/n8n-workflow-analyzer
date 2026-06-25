from __future__ import annotations

from pathlib import Path

from n8n_cost_analyzer.models import RiskFinding, WorkflowRiskReport
from n8n_cost_analyzer.parser import parse_workflow_file
from n8n_cost_analyzer.rules import analyze_workflow
from n8n_cost_analyzer.scoring import score_analysis, score_workflow

FIXTURES = Path(__file__).parent / "fixtures"


def test_simple_workflow_low_score():
    wf = parse_workflow_file(FIXTURES / "simple_webhook_workflow.json")
    findings = analyze_workflow(wf)
    report = WorkflowRiskReport(
        workflow_name=wf.name,
        workflow_id=wf.id,
        active=wf.active,
        node_count=len(wf.nodes),
        trigger_types=(),
        findings=tuple(findings),
    )
    scored = score_workflow(report)
    assert scored.overall_risk_score < 30


def test_ai_workflow_higher_cost_score():
    wf = parse_workflow_file(FIXTURES / "ai_workflow.json")
    findings = analyze_workflow(wf)
    report = WorkflowRiskReport(
        workflow_name=wf.name,
        workflow_id=wf.id,
        active=wf.active,
        node_count=len(wf.nodes),
        trigger_types=(),
        findings=tuple(findings),
    )
    scored = score_workflow(report)
    assert scored.cost_risk_score > 0


def test_loop_workflow_high_score():
    wf = parse_workflow_file(FIXTURES / "loop_http_workflow.json")
    findings = analyze_workflow(wf)
    report = WorkflowRiskReport(
        workflow_name=wf.name,
        workflow_id=wf.id,
        active=wf.active,
        node_count=len(wf.nodes),
        trigger_types=(),
        findings=tuple(findings),
    )
    scored = score_workflow(report)
    assert scored.overall_risk_score >= 30


def test_critical_finding_dominates():
    findings = [
        RiskFinding(
            rule_id="TEST_CRIT",
            severity="critical",
            category="cost",
            message="Critical test",
            recommendation="Fix it",
            workflow_name="Test",
        ),
    ]
    report = WorkflowRiskReport(
        workflow_name="Test",
        workflow_id=None,
        active=None,
        node_count=1,
        trigger_types=(),
        findings=tuple(findings),
    )
    scored = score_workflow(report)
    assert scored.cost_risk_score >= 50
    assert scored.overall_risk_score >= 50


def test_cost_findings_affect_cost_score():
    findings = [
        RiskFinding(
            rule_id="COST1",
            severity="high",
            category="cost",
            message="Cost risk",
            recommendation="Reduce cost",
            workflow_name="Test",
        ),
    ]
    report = WorkflowRiskReport(
        workflow_name="Test",
        workflow_id=None,
        active=None,
        node_count=1,
        trigger_types=(),
        findings=tuple(findings),
    )
    scored = score_workflow(report)
    assert scored.cost_risk_score >= 30
    assert scored.operational_risk_score == 0
    assert scored.complexity_score == 0


def test_score_cap_at_100():
    findings = [
        RiskFinding(
            rule_id=f"HIGH_{i}",
            severity="high",
            category="cost",
            message="Multiple high risks",
            recommendation="Fix",
            workflow_name="Test",
        )
        for i in range(10)
    ]
    report = WorkflowRiskReport(
        workflow_name="Test",
        workflow_id=None,
        active=None,
        node_count=1,
        trigger_types=(),
        findings=tuple(findings),
    )
    scored = score_workflow(report)
    assert scored.cost_risk_score <= 100


def test_score_analysis_returns_summary():
    wf = parse_workflow_file(FIXTURES / "simple_webhook_workflow.json")
    findings = analyze_workflow(wf)
    report = WorkflowRiskReport(
        workflow_name=wf.name,
        workflow_id=wf.id,
        active=wf.active,
        node_count=len(wf.nodes),
        trigger_types=(),
        findings=tuple(findings),
    )
    result = score_analysis([report])
    assert result.score_summary is not None
    assert 0 <= result.score_summary.overall_risk_score <= 100
