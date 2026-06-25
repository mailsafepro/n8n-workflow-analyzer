from __future__ import annotations

from pathlib import Path

from n8n_cost_analyzer.models import N8nNode
from n8n_cost_analyzer.parser import parse_workflow_file
from n8n_cost_analyzer.rules import _is_ai_node, analyze_workflow

FIXTURES = Path(__file__).parent / "fixtures"


def _get_rule_ids(workflow_name: str) -> set[str]:
    path = FIXTURES / f"{workflow_name}"
    wf = parse_workflow_file(path)
    findings = analyze_workflow(wf)
    return {f.rule_id for f in findings}


def test_polling_workflow_has_frequent_polling():
    wf = parse_workflow_file(FIXTURES / "polling_workflow.json")
    findings = analyze_workflow(wf)
    rule_ids = {f.rule_id for f in findings}
    assert "FREQ_POLL" in rule_ids


def test_loop_http_workflow_has_loop_http():
    wf = parse_workflow_file(FIXTURES / "loop_http_workflow.json")
    findings = analyze_workflow(wf)
    rule_ids = {f.rule_id for f in findings}
    assert "LOOP_HTTP" in rule_ids


def test_loop_http_workflow_has_db_in_loop():
    wf = parse_workflow_file(FIXTURES / "loop_http_workflow.json")
    findings = analyze_workflow(wf)
    rule_ids = {f.rule_id for f in findings}
    assert "DB_IN_LOOP" in rule_ids


def test_ai_workflow_has_ai_risk():
    wf = parse_workflow_file(FIXTURES / "ai_workflow.json")
    findings = analyze_workflow(wf)
    rule_ids = {f.rule_id for f in findings}
    assert "AI_NODE" in rule_ids


def test_simple_webhook_workflow_no_high_risks():
    wf = parse_workflow_file(FIXTURES / "simple_webhook_workflow.json")
    findings = analyze_workflow(wf)
    high_severity = [f for f in findings if f.severity in ("high", "critical")]
    assert len(high_severity) == 0


def test_findings_have_required_fields():
    wf = parse_workflow_file(FIXTURES / "polling_workflow.json")
    findings = analyze_workflow(wf)
    for f in findings:
        assert f.rule_id
        assert f.severity in ("low", "medium", "high", "critical")
        assert f.category in ("cost", "operational", "complexity", "reliability", "security")
        assert f.message
        assert f.recommendation
        assert f.workflow_name == "Polling Workflow"


def test_large_workflow_risk():
    from n8n_cost_analyzer.models import N8nNode, N8nWorkflow

    nodes = []
    for i in range(60):
        nodes.append(N8nNode(
            id=f"n{i}", name=f"Node{i}", type="n8n-nodes-base.noOp", parameters={},
        ))
    wf = N8nWorkflow(
        id="large", name="Large WF", active=True, nodes=tuple(nodes),
    )
    findings = analyze_workflow(wf)
    rule_ids = {f.rule_id for f in findings}
    assert "LARGE_WF" in rule_ids


def test_critical_large_workflow():
    from n8n_cost_analyzer.models import N8nNode, N8nWorkflow

    nodes = []
    for i in range(120):
        nodes.append(N8nNode(
            id=f"n{i}", name=f"Node{i}", type="n8n-nodes-base.noOp", parameters={},
        ))
    wf = N8nWorkflow(
        id="huge", name="Huge WF", active=True, nodes=tuple(nodes),
    )
    findings = analyze_workflow(wf)
    criticals = [f for f in findings if f.severity == "critical"]
    assert len(criticals) >= 1


def test_disabled_risky_node_ignored_by_default():
    wf = parse_workflow_file(FIXTURES / "workflow_with_disabled_nodes.json")
    findings = analyze_workflow(wf)
    rule_ids = {f.rule_id for f in findings}
    # FREQ_POLL should fire for active Schedule node
    assert "FREQ_POLL" in rule_ids
    # LOOP_HTTP should NOT fire because HTTP Request is disabled
    assert "AI_NODE" not in rule_ids


def test_disabled_risky_node_included_with_flag():
    wf = parse_workflow_file(FIXTURES / "workflow_with_disabled_nodes.json")
    findings = analyze_workflow(wf, include_disabled=True)
    rule_ids = {f.rule_id for f in findings}
    assert "FREQ_POLL" in rule_ids
    assert "AI_NODE" in rule_ids


def test_high_fan_out_rule():
    wf = parse_workflow_file(FIXTURES / "high_fan_out_workflow.json")
    findings = analyze_workflow(wf)
    rule_ids = {f.rule_id for f in findings}
    assert "HIGH_FAN_OUT" in rule_ids


def test_unknown_node_does_not_crash():
    wf = parse_workflow_file(FIXTURES / "unknown_node_workflow.json")
    findings = analyze_workflow(wf)
    assert isinstance(findings, list)


def test_is_ai_node_no_false_positive_on_non_ai_types():
    non_ai = [
        "n8n-nodes-base.gmailTrigger",
        "n8n-nodes-base.gmailTool",
        "n8n-nodes-base.gmail",
        "n8n-nodes-base.wait",
        "n8n-nodes-base.if",
        "n8n-nodes-base.manualTrigger",
        "n8n-nodes-base.telegramTrigger",
        "n8n-nodes-base.telegram",
        "n8n-nodes-base.scheduleTrigger",
        "n8n-nodes-base.cron",
    ]
    for t in non_ai:
        node = N8nNode(id="x", name="Test", type=t, parameters={})
        assert not _is_ai_node(node), f"{t} should not be classified as AI"


def test_is_ai_node_positive_on_known_ai_types():
    ai_types = [
        "n8n-nodes-base.openAi",
        "n8n-nodes-base.anthropicAi",
        "@n8n/n8n-nodes-langchain.openAi",
        "@n8n/n8n-nodes-langchain.lmChatOpenAi",
        "@n8n/n8n-nodes-langchain.lmChatGoogleGemini",
        "@n8n/n8n-nodes-langchain.lmChatOpenRouter",
        "@n8n/n8n-nodes-langchain.agent",
        "@n8n/n8n-nodes-langchain.chainLlm",
    ]
    for t in ai_types:
        node = N8nNode(id="x", name="Test", type=t, parameters={})
        assert _is_ai_node(node), f"{t} should be classified as AI"


def test_is_ai_node_false_on_infra_types():
    infra_types = [
        "@n8n/n8n-nodes-langchain.memoryBufferWindow",
        "@n8n/n8n-nodes-langchain.documentDefaultDataLoader",
        "@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter",
        "@n8n/n8n-nodes-langchain.outputParserAutofixing",
        "@n8n/n8n-nodes-langchain.outputParserStructured",
        "@n8n/n8n-nodes-langchain.toolVectorStore",
    ]
    for t in infra_types:
        node = N8nNode(id="x", name="Test", type=t, parameters={})
        assert not _is_ai_node(node), f"{t} should NOT be classified as AI cost node"


def test_freq_poll_triggers_on_every_minute_mode():
    from n8n_cost_analyzer.models import N8nNode, N8nWorkflow
    node = N8nNode(
        id="n1", name="Cron", type="n8n-nodes-base.scheduleTrigger",
        parameters={"triggerTimes": {"item": [{"mode": "everyMinute"}]}},
    )
    wf = N8nWorkflow(id="wf", name="Test", active=True, nodes=(node,))
    findings = analyze_workflow(wf)
    rule_ids = {f.rule_id for f in findings}
    assert "FREQ_POLL" in rule_ids


def test_freq_poll_triggers_on_every_5_minutes_mode():
    from n8n_cost_analyzer.models import N8nNode, N8nWorkflow
    node = N8nNode(
        id="n1", name="Cron", type="n8n-nodes-base.scheduleTrigger",
        parameters={"triggerTimes": {"item": [{"mode": "every5Minutes"}]}},
    )
    wf = N8nWorkflow(id="wf", name="Test", active=True, nodes=(node,))
    findings = analyze_workflow(wf)
    rule_ids = {f.rule_id for f in findings}
    assert "FREQ_POLL" in rule_ids


def test_freq_poll_does_not_trigger_on_hourly():
    from n8n_cost_analyzer.models import N8nNode, N8nWorkflow
    node = N8nNode(
        id="n1", name="Hourly", type="n8n-nodes-base.scheduleTrigger",
        parameters={"rule": {"interval": [{"field": "hours", "hoursInterval": 1}]}},
    )
    wf = N8nWorkflow(id="wf", name="Test", active=True, nodes=(node,))
    findings = analyze_workflow(wf)
    rule_ids = {f.rule_id for f in findings}
    assert "FREQ_POLL" not in rule_ids


def test_freq_poll_does_not_trigger_on_daily():
    from n8n_cost_analyzer.models import N8nNode, N8nWorkflow
    node = N8nNode(
        id="n1", name="Daily", type="n8n-nodes-base.scheduleTrigger",
        parameters={"rule": {"interval": [{"field": "days", "daysInterval": 1}]}},
    )
    wf = N8nWorkflow(id="wf", name="Test", active=True, nodes=(node,))
    findings = analyze_workflow(wf)
    rule_ids = {f.rule_id for f in findings}
    assert "FREQ_POLL" not in rule_ids


def test_is_ai_node_positive_on_keyword_in_name():
    node = N8nNode(id="x", name="OpenAI Chat Model", type="n8n-nodes-base.noOp", parameters={})
    assert _is_ai_node(node)


def test_freq_poll_does_not_trigger_on_empty_interval():
    from n8n_cost_analyzer.models import N8nNode, N8nWorkflow
    node = N8nNode(
        id="n1", name="Empty", type="n8n-nodes-base.scheduleTrigger",
        parameters={"rule": {"interval": [{}]}},
    )
    wf = N8nWorkflow(id="wf", name="Test", active=True, nodes=(node,))
    findings = analyze_workflow(wf)
    rule_ids = {f.rule_id for f in findings}
    assert "FREQ_POLL" not in rule_ids


def test_freq_poll_does_not_trigger_on_field_minutes_without_interval_value():
    from n8n_cost_analyzer.models import N8nNode, N8nWorkflow
    node = N8nNode(
        id="n1", name="NoVal", type="n8n-nodes-base.scheduleTrigger",
        parameters={"rule": {"interval": [{"field": "minutes"}]}},
    )
    wf = N8nWorkflow(id="wf", name="Test", active=True, nodes=(node,))
    findings = analyze_workflow(wf)
    rule_ids = {f.rule_id for f in findings}
    assert "FREQ_POLL" not in rule_ids


def test_freq_poll_does_not_trigger_on_trigger_at_hour():
    from n8n_cost_analyzer.models import N8nNode, N8nWorkflow
    node = N8nNode(
        id="n1", name="DailyAt9", type="n8n-nodes-base.scheduleTrigger",
        parameters={"rule": {"interval": [{"triggerAtHour": 9}]}},
    )
    wf = N8nWorkflow(id="wf", name="Test", active=True, nodes=(node,))
    findings = analyze_workflow(wf)
    rule_ids = {f.rule_id for f in findings}
    assert "FREQ_POLL" not in rule_ids


def test_freq_poll_triggers_on_seconds_field():
    from n8n_cost_analyzer.models import N8nNode, N8nWorkflow
    node = N8nNode(
        id="n1", name="Secs", type="n8n-nodes-base.scheduleTrigger",
        parameters={"rule": {"interval": [{"field": "seconds"}]}},
    )
    wf = N8nWorkflow(id="wf", name="Test", active=True, nodes=(node,))
    findings = analyze_workflow(wf)
    rule_ids = {f.rule_id for f in findings}
    assert "FREQ_POLL" in rule_ids


def test_freq_poll_does_not_trigger_on_thirty_minute_interval():
    from n8n_cost_analyzer.models import N8nNode, N8nWorkflow
    node = N8nNode(
        id="n1", name="30Min", type="n8n-nodes-base.scheduleTrigger",
        parameters={"rule": {"interval": [{"field": "minutes", "minutesInterval": 30}]}},
    )
    wf = N8nWorkflow(id="wf", name="Test", active=True, nodes=(node,))
    findings = analyze_workflow(wf)
    rule_ids = {f.rule_id for f in findings}
    assert "FREQ_POLL" not in rule_ids


def test_freq_poll_does_not_trigger_on_zero_minutes_interval():
    from n8n_cost_analyzer.models import N8nNode, N8nWorkflow
    node = N8nNode(
        id="n1", name="Zero", type="n8n-nodes-base.scheduleTrigger",
        parameters={"rule": {"interval": [{"field": "minutes", "minutesInterval": 0}]}},
    )
    wf = N8nWorkflow(id="wf", name="Test", active=True, nodes=(node,))
    findings = analyze_workflow(wf)
    rule_ids = {f.rule_id for f in findings}
    assert "FREQ_POLL" not in rule_ids


def test_freq_poll_triggers_on_one_minute_interval():
    from n8n_cost_analyzer.models import N8nNode, N8nWorkflow
    node = N8nNode(
        id="n1", name="1Min", type="n8n-nodes-base.scheduleTrigger",
        parameters={"rule": {"interval": [{"field": "minutes", "minutesInterval": 1}]}},
    )
    wf = N8nWorkflow(id="wf", name="Test", active=True, nodes=(node,))
    findings = analyze_workflow(wf)
    rule_ids = {f.rule_id for f in findings}
    assert "FREQ_POLL" in rule_ids


def test_freq_poll_triggers_on_five_minute_interval():
    from n8n_cost_analyzer.models import N8nNode, N8nWorkflow
    node = N8nNode(
        id="n1", name="5Min", type="n8n-nodes-base.scheduleTrigger",
        parameters={"rule": {"interval": [{"field": "minutes", "minutesInterval": 5}]}},
    )
    wf = N8nWorkflow(id="wf", name="Test", active=True, nodes=(node,))
    findings = analyze_workflow(wf)
    rule_ids = {f.rule_id for f in findings}
    assert "FREQ_POLL" in rule_ids
