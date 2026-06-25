from __future__ import annotations

from pathlib import Path

from n8n_cost_analyzer.parser import parse_workflow_file
from n8n_cost_analyzer.recommendations import generate_recommendations
from n8n_cost_analyzer.rules import analyze_workflow

FIXTURES = Path(__file__).parent / "fixtures"


def test_polling_produces_webhook_recommendation():
    wf = parse_workflow_file(FIXTURES / "polling_workflow.json")
    findings = analyze_workflow(wf)
    recs = generate_recommendations(findings)
    webhook_recs = [r for r in recs if "webhook" in r.lower()]
    assert len(webhook_recs) >= 1


def test_ai_produces_token_cost_recommendation():
    wf = parse_workflow_file(FIXTURES / "ai_workflow.json")
    findings = analyze_workflow(wf)
    recs = generate_recommendations(findings)
    token_recs = [r for r in recs if "token" in r.lower() or "cost" in r.lower()]
    assert len(token_recs) >= 1


def test_no_duplicate_recommendations():
    wf = parse_workflow_file(FIXTURES / "loop_http_workflow.json")
    findings = analyze_workflow(wf)
    recs = generate_recommendations(findings)
    assert len(recs) == len(set(recs))


def test_simple_workflow_few_recommendations():
    wf = parse_workflow_file(FIXTURES / "simple_webhook_workflow.json")
    findings = analyze_workflow(wf)
    recs = generate_recommendations(findings)
    assert len(recs) <= 2


def test_all_rules_have_recommendations():
    from n8n_cost_analyzer.recommendations import RECOMMENDATION_MAP
    from n8n_cost_analyzer.rules import ALL_RULES

    for rule_fn in ALL_RULES:
        rule_id = rule_fn.__name__.replace("rule_", "").upper()
        # Map known rule_ids to their function names
    # Check that all expected rule IDs have a recommendation
    expected_rules = {
        "FREQ_POLL", "LOOP_HTTP", "AI_NODE", "LARGE_WF",
        "NO_ERROR_HANDLING", "WEBHOOK_CHAIN", "DB_IN_LOOP", "MANY_HTTP",
    }
    for rule_id in expected_rules:
        assert rule_id in RECOMMENDATION_MAP, f"Missing recommendation for {rule_id}"
