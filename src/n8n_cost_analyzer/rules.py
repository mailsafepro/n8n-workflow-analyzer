from __future__ import annotations

from collections.abc import Sequence

from n8n_cost_analyzer.models import N8nNode, N8nWorkflow, RiskFinding, WorkflowRiskReport

SCHEDULE_TRIGGER_TYPES = {
    "n8n-nodes-base.scheduleTrigger",
    "n8n-nodes-base.cron",
    "n8n-nodes-base.interval",
}

LOOP_NODE_TYPES = {
    "n8n-nodes-base.splitInBatches",
    "n8n-nodes-base.loop",
    "n8n-nodes-base.itemLists",
    "n8n-nodes-base.merge",
}

AI_NODE_KEYWORDS = {"openai", "llm", "anthropic", "chatgpt", "gpt", "model"}

AI_NODE_KNOWN_TYPES: set[str] = {
    "n8n-nodes-base.openAi",
    "n8n-nodes-base.anthropicAi",
    "@n8n/n8n-nodes-langchain.openAi",
    "@n8n/n8n-nodes-langchain.lmChatOpenAi",
    "@n8n/n8n-nodes-langchain.lmChatGoogleGemini",
    "@n8n/n8n-nodes-langchain.lmChatOpenRouter",
    "@n8n/n8n-nodes-langchain.agent",
    "@n8n/n8n-nodes-langchain.chainLlm",
    "@n8n/n8n-nodes-langchain.embeddingsGoogleGemini",
    "@tavily/n8n-nodes-tavily.tavilyTool",
    "n8n-nodes-base.perplexity",
}

AI_INFRA_TYPES: set[str] = {
    "@n8n/n8n-nodes-langchain.memoryBufferWindow",
    "@n8n/n8n-nodes-langchain.documentDefaultDataLoader",
    "@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter",
    "@n8n/n8n-nodes-langchain.outputParserAutofixing",
    "@n8n/n8n-nodes-langchain.outputParserStructured",
    "@n8n/n8n-nodes-langchain.toolVectorStore",
}

DB_NODE_TYPES = {
    "n8n-nodes-base.postgres",
    "n8n-nodes-base.mySql",
    "n8n-nodes-base.mySql",
    "n8n-nodes-base.microsoftSql",
    "n8n-nodes-base.snowflake",
    "n8n-nodes-base.mongoDb",
    "n8n-nodes-base.redis",
}

WEBHOOK_TYPES = {"n8n-nodes-base.webhook"}


def _is_schedule_trigger(node: N8nNode) -> bool:
    return node.type in SCHEDULE_TRIGGER_TYPES


def _is_ai_node(node: N8nNode) -> bool:
    if node.type in AI_INFRA_TYPES:
        return False
    if node.type in AI_NODE_KNOWN_TYPES:
        return True
    lower_name = node.name.lower()
    lower_type = node.type.lower()
    for kw in AI_NODE_KEYWORDS:
        if kw in lower_name or kw in lower_type:
            return True
    return False


def _is_http_node(node: N8nNode) -> bool:
    return node.type == "n8n-nodes-base.httpRequest"


def _is_loop_node(node: N8nNode) -> bool:
    return node.type in LOOP_NODE_TYPES


def _is_db_node(node: N8nNode) -> bool:
    return node.type in DB_NODE_TYPES


def _is_webhook(node: N8nNode) -> bool:
    return node.type in WEBHOOK_TYPES


def _get_trigger_types(nodes: tuple[N8nNode, ...]) -> tuple[str, ...]:
    triggers: list[str] = []
    for n in nodes:
        if n.type.endswith("Trigger") or n.type.endswith("trigger") or "schedule" in n.type.lower():
            triggers.append(n.type)
    return tuple(sorted(set(triggers)))


def _active_nodes(nodes: tuple[N8nNode, ...]) -> tuple[N8nNode, ...]:
    return tuple(n for n in nodes if not n.disabled)


def rule_frequent_polling(
    workflow: N8nWorkflow,
    active_nodes: tuple[N8nNode, ...],
) -> list[RiskFinding]:
    findings: list[RiskFinding] = []
    for node in active_nodes:
        if _is_schedule_trigger(node):
            params = node.parameters or {}
            rule_dict = params.get("rule", {})
            interval_items = rule_dict.get("interval", [])
            is_frequent = False
            for item in interval_items:
                field = item.get("field", "")
                value = item.get("minutesInterval", item.get("hoursInterval"))
                if value is not None:
                    try:
                        val = int(value)
                    except (ValueError, TypeError):
                        continue
                    if field == "minutes" and 0 < val <= 5:
                        is_frequent = True
                if field == "seconds":
                    is_frequent = True

            trigger_times = params.get("triggerTimes", {})
            cron_items = trigger_times.get("item", [])
            for item in cron_items:
                mode = item.get("mode", "")
                if mode in ("everyMinute", "every30Seconds", "every10Seconds", "every5Minutes"):
                    is_frequent = True

            if is_frequent:
                findings.append(RiskFinding(
                    rule_id="FREQ_POLL",
                    severity="high",
                    category="cost",
                    message=f"Frequent polling trigger '{node.name}' can create high execution volume",
                    recommendation="Replace frequent polling with webhook or event-based trigger when possible",
                    workflow_name=workflow.name,
                    node_names=(node.name,),
                ))
    return findings


def rule_loop_http(
    workflow: N8nWorkflow,
    active_nodes: tuple[N8nNode, ...],
) -> list[RiskFinding]:
    findings: list[RiskFinding] = []
    has_loop = any(_is_loop_node(n) for n in active_nodes)
    has_http = any(_is_http_node(n) for n in active_nodes)
    if has_loop and has_http:
        loop_nodes = [n.name for n in active_nodes if _is_loop_node(n)]
        http_nodes = [n.name for n in active_nodes if _is_http_node(n)]
        findings.append(RiskFinding(
            rule_id="LOOP_HTTP",
            severity="high",
            category="cost",
            message="HTTP Request node inside a loop/batch can multiply API calls and costs",
            recommendation="Add rate limits, concurrency controls, or move HTTP calls outside the loop",
            workflow_name=workflow.name,
            node_names=tuple(loop_nodes + http_nodes),
        ))
    return findings


def rule_ai_nodes(
    workflow: N8nWorkflow,
    active_nodes: tuple[N8nNode, ...],
) -> list[RiskFinding]:
    findings: list[RiskFinding] = []
    for node in active_nodes:
        if _is_ai_node(node):
            findings.append(RiskFinding(
                rule_id="AI_NODE",
                severity="medium",
                category="cost",
                message=f"AI/LLM node '{node.name}' has variable token-based cost that can escalate",
                recommendation="Estimate token/API cost before production; set usage limits and monitor spend",
                workflow_name=workflow.name,
                node_names=(node.name,),
            ))
    return findings


def rule_large_workflow(
    workflow: N8nWorkflow,
    active_nodes: tuple[N8nNode, ...],
) -> list[RiskFinding]:
    findings: list[RiskFinding] = []
    n = len(active_nodes)
    if n > 100:
        findings.append(RiskFinding(
            rule_id="LARGE_WF",
            severity="critical",
            category="complexity",
            message=f"Workflow has {n} nodes, making it very complex to maintain and debug",
            recommendation="Split into smaller workflows with clear responsibilities",
            workflow_name=workflow.name,
            node_names=(),
        ))
    elif n > 50:
        findings.append(RiskFinding(
            rule_id="LARGE_WF",
            severity="medium",
            category="complexity",
            message=f"Workflow has {n} nodes, which increases complexity",
            recommendation="Consider splitting into smaller workflows",
            workflow_name=workflow.name,
            node_names=(),
        ))
    return findings


def rule_missing_error_handling(
    workflow: N8nWorkflow,
    active_nodes: tuple[N8nNode, ...],
) -> list[RiskFinding]:
    findings: list[RiskFinding] = []
    settings = workflow.settings or {}
    error_workflow = settings.get("errorWorkflow", settings.get("error_workflow"))
    if not error_workflow:
        has_http = any(_is_http_node(n) for n in active_nodes)
        has_critical = has_http or any(
            n.type in {"n8n-nodes-base.emailSend"} for n in active_nodes
        )
        if has_critical or len(active_nodes) > 10:
            findings.append(RiskFinding(
                rule_id="NO_ERROR_HANDLING",
                severity="medium",
                category="reliability",
                message="Workflow has no error workflow configured",
                recommendation="Configure an error workflow to handle failures gracefully",
                workflow_name=workflow.name,
                node_names=(),
            ))
    return findings


def rule_possible_webhook_chain(
    workflow: N8nWorkflow,
    active_nodes: tuple[N8nNode, ...],
) -> list[RiskFinding]:
    findings: list[RiskFinding] = []
    webhook_nodes = [n for n in active_nodes if _is_webhook(n)]
    http_nodes = [n for n in active_nodes if _is_http_node(n)]
    if webhook_nodes and http_nodes:
        for wn in webhook_nodes:
            for hn in http_nodes:
                params = hn.parameters or {}
                url = str(params.get("url", ""))
                if "webhook" in url.lower() or "/webhook/" in url:
                    findings.append(RiskFinding(
                        rule_id="WEBHOOK_CHAIN",
                        severity="medium",
                        category="operational",
                        message=f"Webhook '{wn.name}' + HTTP to webhook URL may create cascading chains",
                        recommendation="Review webhook chain depth; add idempotency guards to prevent duplicate processing",  # noqa: E501
                        workflow_name=workflow.name,
                        node_names=(wn.name, hn.name),
                    ))
                    break
        if not findings:
            findings.append(RiskFinding(
                rule_id="WEBHOOK_CHAIN",
                severity="low",
                category="operational",
                message=f"Webhook '{webhook_nodes[0].name}' triggers external HTTP calls — cascading chain risk",
                recommendation="Review if webhook triggers downstream workflows; add idempotency",
                workflow_name=workflow.name,
                node_names=(webhook_nodes[0].name,),
            ))
    return findings


def rule_db_in_loop(
    workflow: N8nWorkflow,
    active_nodes: tuple[N8nNode, ...],
) -> list[RiskFinding]:
    findings: list[RiskFinding] = []
    has_loop = any(_is_loop_node(n) for n in active_nodes)
    has_db = any(_is_db_node(n) for n in active_nodes)
    if has_loop and has_db:
        loop_nodes = [n.name for n in active_nodes if _is_loop_node(n)]
        db_nodes = [n.name for n in active_nodes if _is_db_node(n)]
        findings.append(RiskFinding(
            rule_id="DB_IN_LOOP",
            severity="high",
            category="operational",
            message="Database operation inside a loop can cause performance issues and unexpected costs",
            recommendation="Move DB operations outside the loop or batch them",
            workflow_name=workflow.name,
            node_names=tuple(loop_nodes + db_nodes),
        ))
    return findings


def rule_many_http_calls(
    workflow: N8nWorkflow,
    active_nodes: tuple[N8nNode, ...],
) -> list[RiskFinding]:
    findings: list[RiskFinding] = []
    http_nodes = [n for n in active_nodes if _is_http_node(n)]
    if len(http_nodes) >= 3:
        findings.append(RiskFinding(
            rule_id="MANY_HTTP",
            severity="low",
            category="cost",
            message=f"Workflow has {len(http_nodes)} HTTP Request nodes, increasing external dependency and cost",
            recommendation="Review if all HTTP calls are necessary; consider caching or batching",
            workflow_name=workflow.name,
            node_names=tuple(n.name for n in http_nodes),
        ))
    return findings


def rule_high_fan_out(
    workflow: N8nWorkflow,
    active_nodes: tuple[N8nNode, ...],
) -> list[RiskFinding]:
    findings: list[RiskFinding] = []
    connections = workflow.connections or {}
    outgoing_counts: dict[str, int] = {}
    for source_name, outputs in connections.items():
        if isinstance(outputs, dict):
            for output_arrays in outputs.values():
                if isinstance(output_arrays, list):
                    for output_index in output_arrays:
                        if isinstance(output_index, list):
                            for c in output_index:
                                if isinstance(c, dict):
                                    target = c.get("node", "")
                                    if target:
                                        outgoing_counts[source_name] = outgoing_counts.get(source_name, 0) + 1

    for node_name, count in outgoing_counts.items():
        if count >= 5:
            findings.append(RiskFinding(
                rule_id="HIGH_FAN_OUT",
                severity="medium",
                category="complexity",
                message=f"Node '{node_name}' has {count} outgoing connections (high fan-out)",
                recommendation="Review branching logic; consider splitting into sub-workflows or reducing fan-out",
                workflow_name=workflow.name,
                node_names=(node_name,),
            ))
    return findings


ALL_RULES: list = [
    rule_frequent_polling,
    rule_loop_http,
    rule_ai_nodes,
    rule_large_workflow,
    rule_missing_error_handling,
    rule_possible_webhook_chain,
    rule_db_in_loop,
    rule_many_http_calls,
    rule_high_fan_out,
]


def analyze_workflow(
    workflow: N8nWorkflow,
    include_disabled: bool = False,
) -> list[RiskFinding]:
    active_nodes = workflow.nodes if include_disabled else _active_nodes(workflow.nodes)
    findings: list[RiskFinding] = []
    for rule_fn in ALL_RULES:
        findings.extend(rule_fn(workflow, active_nodes))
    return findings


def analyze_workflows(
    workflows: Sequence[N8nWorkflow],
    include_disabled: bool = False,
) -> list[WorkflowRiskReport]:
    reports: list[WorkflowRiskReport] = []
    for wf in workflows:
        findings = analyze_workflow(wf, include_disabled=include_disabled)
        trigger_types = _get_trigger_types(wf.nodes)
        report = WorkflowRiskReport(
            workflow_name=wf.name,
            workflow_id=wf.id,
            active=wf.active,
            node_count=len(wf.nodes),
            trigger_types=trigger_types,
            findings=tuple(findings),
        )
        reports.append(report)
    return reports
