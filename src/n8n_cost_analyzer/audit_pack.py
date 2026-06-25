from __future__ import annotations

from pathlib import Path

from n8n_cost_analyzer.json_report import write_json_report
from n8n_cost_analyzer.models import AnalysisResult, CostModel
from n8n_cost_analyzer.report import _maybe_truncate, _remaining_note, generate_markdown_report
from n8n_cost_analyzer.text_helpers import pluralize
from n8n_cost_analyzer.version import __version__


def _severity_label(score: int) -> str:
    if score >= 70:
        return "Critical"
    if score >= 40:
        return "High"
    if score >= 20:
        return "Medium"
    if score > 0:
        return "Low"
    return "None"


def _risk_level_badge(score: int) -> str:
    if score >= 70:
        return "🔴 Critical"
    if score >= 40:
        return "🟡 High"
    if score >= 20:
        return "🟠 Medium"
    if score > 0:
        return "🟢 Low"
    return "⚪ None"


def derive_business_impact_labels(result: AnalysisResult) -> list[str]:
    labels: list[str] = []
    all_findings = [f for r in result.reports for f in r.findings]
    rule_ids = {f.rule_id for f in all_findings}
    categories = {f.category for f in all_findings}
    severities = {f.severity for f in all_findings}

    cost_high = any(
        f.category == "cost" and f.severity in ("high", "critical")
        for f in all_findings
    )
    if cost_high:
        labels.append("High cost exposure")
    elif "cost" in categories and any(f.severity == "medium" for f in all_findings if f.category == "cost"):
        labels.append("Moderate cost exposure")

    if "LOOP_HTTP" in rule_ids or "HIGH_FAN_OUT" in rule_ids or "WEBHOOK_CHAIN" in rule_ids:
        labels.append("Runaway execution risk")

    if "NO_ERROR_HANDLING" in rule_ids:
        labels.append("Reliability risk")

    if "LARGE_WF" in rule_ids:
        labels.append("Maintainability risk")

    if result.node_inventory and result.node_inventory.unknown_node_types:
        labels.append("Unknown/custom node risk")

    if result.node_inventory and result.node_inventory.credential_reference_count > 0:
        labels.append("Credential governance review needed")

    if "AI_NODE" in rule_ids:
        labels.append("AI/API variable cost risk")

    if "critical" in severities:
        labels.append("Critical risk items require immediate attention")

    return labels


def _concentration_label(drivers: tuple[str, ...]) -> str:
    count = len(drivers)
    if count >= 3:
        return "High"
    if count >= 1:
        return "Medium"
    return "Low"


def _workflows_with_rule(result: AnalysisResult, rule_id: str) -> list:
    return [r for r in result.reports if any(f.rule_id == rule_id for f in r.findings)]


def generate_executive_summary(
    result: AnalysisResult,
    cost_model: CostModel | None = None,
) -> str:
    lines: list[str] = []
    s = result.score_summary
    all_findings = [f for r in result.reports for f in r.findings]
    total_critical = sum(1 for f in all_findings if f.severity == "critical")
    total_high = sum(1 for f in all_findings if f.severity == "high")
    total_medium = sum(1 for f in all_findings if f.severity == "medium")
    total_low = sum(1 for f in all_findings if f.severity == "low")
    workflow_count = len(result.reports)

    lines.append("# Executive Summary — n8n Workflow Cost & Risk Audit")
    lines.append("")

    # =========================================================
    # How to Read This Report
    lines.append("## How to Read This Report")
    lines.append("")
    lines.append("Start with **Overall Assessment** for a quick score overview.")
    lines.append("Then **Portfolio Insights** and **Top Risk Patterns** for what matters most.")
    lines.append("Use **Top Workflows To Review** for specific remediation targets.")
    lines.append("The **What To Do First** section provides concrete next steps.")
    lines.append("")

    # =========================================================
    # Overall Assessment
    lines.append("## Overall Assessment")
    lines.append("")
    has_reliability = any(f.category == "reliability" for f in all_findings)
    op_score = s.operational_risk_score
    if has_reliability and op_score == 0:
        op_label = f"🟠 Review ({op_score}/100) — reliability findings present"
    else:
        op_label = f"{_risk_level_badge(op_score)} ({op_score}/100)"
    lines.append(f"- **Workflows analyzed:** {pluralize(workflow_count, 'workflow')}")
    lines.append(f"- **Overall portfolio risk:** {_risk_level_badge(s.overall_risk_score)} ({s.overall_risk_score}/100)")
    lines.append(f"- **Cost risk:** {_risk_level_badge(s.cost_risk_score)} ({s.cost_risk_score}/100)")
    lines.append(f"- **Operational / reliability risk:** {op_label}")
    lines.append(f"- **Complexity risk:** {_risk_level_badge(s.complexity_score)} ({s.complexity_score}/100)")
    finding_parts = []
    if total_critical > 0:
        finding_parts.append(pluralize(total_critical, "critical finding"))
    if total_high > 0:
        finding_parts.append(pluralize(total_high, "high finding"))
    if total_medium > 0:
        finding_parts.append(pluralize(total_medium, "medium finding"))
    if total_low > 0:
        finding_parts.append(pluralize(total_low, "low finding"))
    finding_summary = ", ".join(finding_parts)
    lines.append(
        f"- **Total findings:** {pluralize(len(all_findings), 'finding')} ({finding_summary})"
    )
    if result.workflow_rankings:
        lines.append(f"- **Most urgent workflow:** {result.workflow_rankings[0].workflow_name}")
    lines.append("")

    # =========================================================
    # Portfolio Insights
    lines.append("## Portfolio Insights")
    lines.append("")

    ai_workflows = _workflows_with_rule(result, "AI_NODE")
    ai_wf_count = len(ai_workflows)
    no_handle_workflows = _workflows_with_rule(result, "NO_ERROR_HANDLING")
    no_handle_count = len(no_handle_workflows)
    loop_http_workflows = _workflows_with_rule(result, "LOOP_HTTP")
    loop_http_count = len(loop_http_workflows)
    cred_count = result.node_inventory.credential_reference_count if result.node_inventory else 0

    high_risk_count = sum(1 for r in result.reports if r.overall_risk_score >= 40)

    insights: list[str] = []

    if workflow_count > 0 and ai_wf_count > 0:
        ai_pct = round(ai_wf_count / workflow_count * 100)
        insights.append(
            f"~{ai_pct}% of workflows ({ai_wf_count}/{workflow_count}) "
            "contain AI/API nodes with variable token-based costs."
        )

    if no_handle_count > 0:
        nh_pct = round(no_handle_count / workflow_count * 100)
        insights.append(
            f"~{nh_pct}% of workflows ({no_handle_count}/{workflow_count}) "
            "lack error handling — silent failures are likely."
        )

    if result.workflow_rankings:
        top5_sum = sum(e.finding_count for e in result.workflow_rankings[:5])
        top5_pct = round(top5_sum / len(all_findings) * 100) if all_findings else 0
        insights.append(
            f"A small subset (top 5 workflows) concentrates ~{top5_pct}% of all findings "
            f"({top5_sum}/{len(all_findings)})."
        )

    avg_findings = round(len(all_findings) / workflow_count, 1) if workflow_count > 0 else 0
    insights.append(f"Average of ~{avg_findings} findings per workflow.")

    non_zero = sum(1 for r in result.reports if r.overall_risk_score > 0)
    if non_zero > 0:
        insights.append(
            f"{pluralize(high_risk_count, 'workflow')} ha{'s' if high_risk_count == 1 else 've'} "
            "review-worthy risk patterns (score ≥ 40); the rest are low or zero risk."
        )

    for ins in insights:
        lines.append(f"- {ins}")
    lines.append("")

    # Interpretation
    lines.append("**Interpretation:**")
    interp_parts: list[str] = []
    if ai_wf_count > workflow_count / 2:
        interp_parts.append("AI/API cost exposure is the dominant risk factor across the portfolio.")
    if no_handle_count > workflow_count / 2:
        interp_parts.append("Most workflows share a systemic reliability gap (no error handling).")
    interp_parts.append(
        "Risk is unevenly distributed — remediation can focus on a subset of "
        "workflows and patterns rather than the entire portfolio."
    )
    lines.append(" ".join(interp_parts))
    lines.append("")

    # =========================================================
    # Top Risk Patterns Detected
    lines.append("## Top Risk Patterns Detected")
    lines.append("")

    patterns: list[tuple[str, str, int, str, str]] = []

    # 1. AI/API cost exposure
    ai_finding_count = sum(1 for f in all_findings if f.rule_id == "AI_NODE")
    if ai_finding_count > 0:
        patterns.append((
            "AI/API cost exposure",
            f"{pluralize(ai_wf_count, 'workflow')}, {pluralize(ai_finding_count, 'occurrence')}",
            ai_finding_count,
            "AI_NODE — AI/LLM nodes with token-based pricing",
            "Variable and potentially unbounded costs per workflow execution; "
            "cost scales with input complexity and volume"
        ))

    # 2. Missing error handling
    nh_finding_count = sum(1 for f in all_findings if f.rule_id == "NO_ERROR_HANDLING")
    if nh_finding_count > 0:
        patterns.append((
            "Missing error handling",
            f"{pluralize(no_handle_count, 'workflow')}",
            nh_finding_count,
            "NO_ERROR_HANDLING — no error workflow configured",
            "Silent failures, undetected outages, and potential data loss on execution errors"
        ))

    # 3. High external API usage
    many_http_workflows = _workflows_with_rule(result, "MANY_HTTP")
    many_http_count = len(many_http_workflows)
    all_http_count = sum(1 for f in all_findings if f.rule_id in ("MANY_HTTP", "LOOP_HTTP"))
    http_wf_union = set()
    for r in _workflows_with_rule(result, "MANY_HTTP"):
        http_wf_union.add(r.workflow_name)
    for r in _workflows_with_rule(result, "LOOP_HTTP"):
        http_wf_union.add(r.workflow_name)
    if many_http_count > 0 or loop_http_count > 0:
        patterns.append((
            "High external API usage",
            f"{pluralize(len(http_wf_union), 'workflow')}, {pluralize(all_http_count, 'occurrence')}",
            all_http_count,
            "MANY_HTTP / LOOP_HTTP — multiple HTTP nodes or loops containing HTTP calls",
            "Cost, latency, and external dependency risk; loops can amplify API usage multiplicatively"
        ))

    # 4. Loop-based scaling risks
    if loop_http_count > 0:
        lh_finding_count = sum(1 for f in all_findings if f.rule_id == "LOOP_HTTP")
        patterns.append((
            "Loop-based scaling risks",
            f"{pluralize(loop_http_count, 'workflow')}, {pluralize(lh_finding_count, 'occurrence')}",
            lh_finding_count,
            "LOOP_HTTP — HTTP requests inside loop or batch logic",
            "Multiplicative execution cost; batch size directly multiplies API calls and LLM tokens"
        ))

    # 5. Large or complex workflows
    large_wf_count = len(_workflows_with_rule(result, "LARGE_WF"))
    high_fanout_count = len(_workflows_with_rule(result, "HIGH_FAN_OUT"))
    if large_wf_count > 0 or high_fanout_count > 0:
        total_complex = sum(
            1 for r in result.reports
            if any(f.rule_id in ("LARGE_WF", "HIGH_FAN_OUT") for f in r.findings)
        )
        complex_findings = sum(
            1 for f in all_findings if f.rule_id in ("LARGE_WF", "HIGH_FAN_OUT")
        )
        patterns.append((
            "Large or complex workflows",
            f"{pluralize(total_complex, 'workflow')}, {pluralize(complex_findings, 'occurrence')}",
            complex_findings,
            "LARGE_WF / HIGH_FAN_OUT — oversized workflows or excessive branching",
            "Reduced maintainability, harder debugging, and unexpected API load from fan-out nodes"
        ))

    patterns.sort(key=lambda x: -x[2])

    for i, (title, scope, _count, cause, impact) in enumerate(patterns, 1):
        lines.append(f"{i}. **{title}** — {scope}")
        lines.append(f"   → Caused by: {cause}")
        lines.append(f"   → Impact: {impact}")
        lines.append("")

    # =========================================================
    # Top Workflows To Review
    lines.append("## Top Workflows To Review")
    lines.append("")
    if result.workflow_rankings:
        has_any_critical = any(f.severity == "critical" for f in all_findings)
        lines.append("| # | Workflow | Review Priority | Risk Drivers | Concentration | Suggested Action |")
        lines.append("|---|----------|-----------------|--------------|---------------|------------------|")
        for entry in result.workflow_rankings[:5]:
            priority = _review_priority_label(entry.overall_risk_score, has_any_critical, entry.critical_count)
            drivers = entry.top_risk_drivers[:3] if entry.top_risk_drivers else ("—",)
            concentration = _concentration_label(entry.top_risk_drivers)
            action = _suggested_action(drivers)
            lines.append(
                f"| {entry.rank} | {entry.workflow_name} | {priority} | "
                f"{', '.join(drivers)} | {concentration} | {action} |"
            )
    else:
        lines.append("No workflows to review.")
    lines.append("")

    # =========================================================
    # Cost Exposure Overview
    lines.append("## Cost Exposure Overview")
    lines.append("")

    cost_lines: list[str] = []
    if ai_wf_count > 0:
        cost_lines.append(f"- {pluralize(ai_wf_count, 'workflow')} {'contains' if ai_wf_count == 1 else 'contain'} "
                          "AI/API cost-sensitive nodes.")

    poll_workflows = _workflows_with_rule(result, "FREQ_POLL")
    if poll_workflows:
        cost_lines.append(
            f"- {pluralize(len(poll_workflows), 'workflow')} {'uses' if len(poll_workflows) == 1 else 'use'} "
            "high-frequency triggers or polling patterns."
        )

    if loop_http_count > 0:
        cost_lines.append(
            f"- {pluralize(loop_http_count, 'workflow')} {'contains' if loop_http_count == 1 else 'contain'} "
            "loop + HTTP combinations — multiplicative execution cost."
        )

    if many_http_count > 0:
        cost_lines.append(
            f"- {pluralize(many_http_count, 'workflow')} ha{'s' if many_http_count == 1 else 've'} "
            "multiple external HTTP calls, increasing dependency costs."
        )

    # Workflows with both LOOP_HTTP and AI_NODE
    loop_ai_wf = [r for r in result.reports
                   if any(f.rule_id == "LOOP_HTTP" for f in r.findings)
                   and any(f.rule_id == "AI_NODE" for f in r.findings)]
    if loop_ai_wf:
        cost_lines.append(
            f"- {pluralize(len(loop_ai_wf), 'workflow')} combine{'s' if len(loop_ai_wf) == 1 else ''} "
            "loops with AI/API nodes — highest cost uncertainty."
        )

    for cl in cost_lines:
        lines.append(cl)
    lines.append("")
    lines.append(
        "AI/API nodes represent variable cost, while loops and polling can amplify execution count. "
        "Together, these create the highest cost uncertainty in the portfolio."
    )
    lines.append("")

    # =========================================================
    # Credential Footprint
    lines.append("## Credential Footprint")
    lines.append("")

    if result.node_inventory and cred_count > 0:
        avg_cred = round(cred_count / workflow_count, 1) if workflow_count > 0 else 0
        lines.append(f"- **Total credential references:** {cred_count}")
        lines.append(f"- **Average per workflow:** ~{avg_cred}")

        if result.workflows_extra:
            wf_creds = [(we.credential_reference_count, r.workflow_name)
                        for we, r in zip(result.workflows_extra, result.reports)]
            wf_creds.sort(key=lambda x: -x[0])
            if wf_creds and wf_creds[0][0] > 0:
                lines.append(f"- **Highest concentration:** {wf_creds[0][1]} ({wf_creds[0][0]} references)")

        unk_count = len(result.node_inventory.unknown_node_types) if result.node_inventory.unknown_node_types else 0
        if unk_count > 0:
            lines.append(f"- **Custom/community node types:** {unk_count} — may have unknown credential patterns")

        lines.append("")
        if cred_count < workflow_count:
            cred_wording = "Credential references are present but not widespread in this export."
        elif avg_cred < 3:
            cred_wording = "Credential usage appears common across the portfolio."
        else:
            cred_wording = "Credential usage is widespread across the automation portfolio."
        lines.append(cred_wording)
        lines.append("This increases the importance of:")
        lines.append("- proper credential scoping and rotation policies")
        lines.append("- avoiding reuse across unrelated workflows")
        lines.append("- auditing custom node credential handling")
    else:
        lines.append("No credential references detected.")
    lines.append("")

    # =========================================================
    # Business Impact
    lines.append("## Business Impact")
    lines.append("")

    lines.append("### Cost Risk")
    if ai_wf_count > 0:
        lines.append(f"- AI/API usage introduces variable and hard-to-predict costs across {pluralize(ai_wf_count, 'workflow')}.")
    if loop_http_count > 0:
        lines.append(f"- Loop + HTTP patterns can multiply API usage unexpectedly in {pluralize(loop_http_count, 'workflow')}.")
    if many_http_count > 0:
        lines.append(f"- {pluralize(many_http_count, 'workflow')} make{'s' if many_http_count == 1 else ''} "
                     "many external HTTP calls, increasing dependency costs.")
    if not ai_wf_count and not loop_http_count and not many_http_count:
        lines.append("- No significant cost risk identified.")
    lines.append("")

    lines.append("### Reliability Risk")
    if no_handle_count > 0:
        lines.append(f"- {pluralize(no_handle_count, 'workflow')} lack{'s' if no_handle_count == 1 else ''} "
                     "error handling — silent failures may go undetected.")
    webhook_chain_wf = _workflows_with_rule(result, "WEBHOOK_CHAIN")
    if webhook_chain_wf:
        lines.append(f"- {pluralize(len(webhook_chain_wf), 'workflow')} with webhook chains — cascading failure risk.")
    db_in_loop_wf = _workflows_with_rule(result, "DB_IN_LOOP")
    if db_in_loop_wf:
        lines.append(f"- {pluralize(len(db_in_loop_wf), 'workflow')} run{'s' if len(db_in_loop_wf) == 1 else ''} "
                     "database operations in loops — risk of performance degradation.")
    if not no_handle_count and not webhook_chain_wf and not db_in_loop_wf:
        lines.append("- No significant reliability risk identified.")
    lines.append("")

    lines.append("### Operational Complexity")
    fanout_wf = _workflows_with_rule(result, "HIGH_FAN_OUT")
    if fanout_wf:
        lines.append(f"- {pluralize(len(fanout_wf), 'workflow')} ha{'s' if len(fanout_wf) == 1 else 've'} "
                     "high fan-out nodes, increasing debugging difficulty.")
    large_wf = _workflows_with_rule(result, "LARGE_WF")
    if large_wf:
        lines.append(f"- {pluralize(len(large_wf), 'workflow')} {'is' if len(large_wf) == 1 else 'are'} "
                     "large enough to be harder to maintain and debug.")
    unk_count = (
        len(result.node_inventory.unknown_node_types)
        if result.node_inventory and result.node_inventory.unknown_node_types
        else 0
    )
    if unk_count > 0:
        lines.append(f"- {pluralize(unk_count, 'custom/community node type')} introduce{'s' if unk_count == 1 else ''} "
                     "dependency and compatibility risk.")
    if not fanout_wf and not large_wf and unk_count == 0:
        lines.append("- No significant operational complexity identified.")
    lines.append("")

    lines.append("### Governance")
    if cred_count > 0:
        lines.append(f"- {pluralize(cred_count, 'credential reference')} across all workflows suggest need for governance.")
        lines.append("- Credential reuse and rotation policies should be reviewed.")
        lines.append("- Workflow ownership and credential scoping should be documented.")
    if unk_count > 0:
        lines.append(f"- {pluralize(unk_count, 'custom node type')} — verify support status and credential handling.")
    if cred_count == 0 and unk_count == 0:
        lines.append("- No significant governance issues identified.")
    lines.append("")

    # =========================================================
    # What To Do First
    lines.append("## What To Do First")
    lines.append("")

    action_steps: list[str] = []

    if result.workflow_rankings:
        top3 = result.workflow_rankings[:3]
        top3_names = ", ".join(e.workflow_name for e in top3)
        top3_drivers = set()
        for e in top3:
            top3_drivers.update(e.top_risk_drivers)
        has_loop = "LOOP_HTTP" in top3_drivers
        has_ai = "AI_NODE" in top3_drivers
        urgency = "immediately" if total_critical > 0 else "first"
        if has_loop:
            action_steps.append(
                f"Review the top 3 highest-risk workflows {urgency} — "
                f"add rate limits to loop + HTTP patterns ({top3_names})."
            )
        elif has_ai:
            action_steps.append(
                f"Review the top 3 highest-risk workflows {urgency} — "
                f"estimate and monitor AI/API costs ({top3_names})."
            )
        else:
            action_steps.append(
                f"Review the top 3 highest-risk workflows {urgency} ({top3_names})."
            )

    if no_handle_count > 0:
        action_steps.append(
            f"Add error handling to {pluralize(no_handle_count, 'workflow')} currently without it."
        )

    if ai_wf_count > 0:
        action_steps.append(
            f"Set usage limits and monitoring on AI/API nodes in {pluralize(ai_wf_count, 'workflow')}."
        )

    if loop_http_count > 0:
        action_steps.append(
            f"Inspect loop + HTTP combinations in {pluralize(loop_http_count, 'workflow')} "
            "for cost amplification risk."
        )

    if cred_count > 0:
        action_steps.append(
            "Review credential usage across the portfolio — identify ownership and rotation needs."
        )

    for i, step in enumerate(action_steps, 1):
        lines.append(f"{i}. {step}")
    lines.append("")

    # =========================================================
    # Recommended Next Step
    cost_high_workflows = sum(
        1 for r in result.reports
        if any(f.category == "cost" and f.severity in ("high", "critical") for f in r.findings)
    )
    lines.append("## Recommended Next Step")
    lines.append("")
    if total_critical > 0:
        next_step = "Review critical-risk workflows immediately before production deployment."
    elif total_high > 0:
        next_step = "Prioritize high-risk workflows for review in the next sprint."
    elif cost_high_workflows > 0:
        next_step = "Prioritize cost-risk workflows to prevent unexpected cloud/API spend."
    elif result.workflow_rankings:
        next_step = "Run a deeper workflow-by-workflow audit for the top-ranked workflows."
    else:
        next_step = "Add monitoring and guardrails to maintain current risk level."
    lines.append(f"> {next_step}")
    lines.append("")

    # =========================================================
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
    lines.append("The portfolio score can be low even if individual workflows have high scores.")
    lines.append("Always check the workflow rankings for the most urgent items.")
    lines.append("")

    # =========================================================
    # Caveats
    lines.append("## Caveats")
    lines.append("")
    lines.append("This analysis is based on static workflow definitions only. The following limitations apply:")
    lines.append("")
    lines.append("- Heuristic analysis based on node types and patterns, not actual execution data.")
    lines.append("- Cost estimates are approximate and derived from configurable assumptions.")
    lines.append("- No runtime metrics, execution logs, or production monitoring data were used.")
    lines.append("- No credentials or secrets were inspected.")
    lines.append("- Actual costs depend on trigger frequency, input data volume, and external API pricing.")
    lines.append("")

    lines.append("---")
    lines.append(f"*Generated by n8n Cost Analyzer v{__version__} — Audit Pack*")
    return "\n".join(lines)


def _review_priority_label(score: int, has_any_critical: bool, workflow_critical_count: int) -> str:
    if has_any_critical and workflow_critical_count > 0:
        return "Critical"
    if score >= 90:
        return "Highest priority"
    if score >= 70:
        return "High priority"
    if score >= 40:
        return "Review recommended"
    if score >= 20:
        return "Moderate"
    return "Low"


def _suggested_action(drivers: tuple[str, ...]) -> str:
    mapping: dict[str, str] = {
        "FREQ_POLL": "Replace polling with webhooks",
        "LOOP_HTTP": "Add rate limits and guards",
        "AI_NODE": "Estimate and monitor token costs",
        "LARGE_WF": "Split into smaller workflows",
        "NO_ERROR_HANDLING": "Configure error workflow",
        "WEBHOOK_CHAIN": "Review cascading triggers",
        "DB_IN_LOOP": "Move DB ops outside loop",
        "MANY_HTTP": "Review external API calls",
        "HIGH_FAN_OUT": "Reduce branching complexity",
    }
    for d in drivers:
        if d in mapping:
            return mapping[d]
    return "Review and assess"


def generate_client_action_plan(
    result: AnalysisResult,
    cost_model: CostModel | None = None,
) -> str:
    lines: list[str] = []
    all_findings = [f for r in result.reports for f in r.findings]
    rule_ids = {f.rule_id for f in all_findings}

    lines.append("# Client Action Plan — n8n Workflow Audit")
    lines.append("")

    # How to read
    lines.append("## How to Read This Plan")
    lines.append("")
    lines.append("This plan is organized by priority. Start with Priority 0, then work through")
    lines.append("Cost Controls, Reliability, and Maintainability. The 7-day plan at the end")
    lines.append("provides a suggested schedule.")
    lines.append("")

    # Priority 0 — Highest-Risk Workflows
    lines.append("## Priority 0 — Highest-Risk Workflows")
    lines.append("")
    critical_findings = [f for f in all_findings if f.severity == "critical"]
    if critical_findings:
        lines.append("The following items require immediate attention:")
        lines.append("")
        for f in critical_findings:
            lines.append(f"- [{f.severity.upper()}] {f.workflow_name}: {f.message}")
    else:
        lines.append("No critical-severity findings were detected.")
        top_wfs = result.workflow_rankings[:3] if result.workflow_rankings else []
        if top_wfs:
            lines.append("The workflows below still deserve early review because they have the highest overall risk scores:")
            lines.append("")
            for entry in top_wfs:
                lines.append(f"- **{entry.workflow_name}** — Risk score: {entry.overall_risk_score}/100")
    lines.append("")

    # Priority 1 — Cost Controls
    lines.append("## Priority 1 — Cost Controls")
    lines.append("")
    cost_actions: list[str] = []
    if "FREQ_POLL" in rule_ids:
        poll_workflows = [r for r in result.reports if any(f.rule_id == "FREQ_POLL" for f in r.findings)]
        names = ", ".join(r.workflow_name for r in poll_workflows)
        cost_actions.append(f"Replace frequent polling triggers in {names} with webhook or event-based triggers.")
    if "LOOP_HTTP" in rule_ids:
        loop_workflows = [r for r in result.reports if any(f.rule_id == "LOOP_HTTP" for f in r.findings)]
        names = ", ".join(r.workflow_name for r in loop_workflows)
        cost_actions.append(f"Add rate limits, concurrency controls, or move HTTP calls outside loops in {names}.")
    if "AI_NODE" in rule_ids:
        ai_workflows = [r for r in result.reports if any(f.rule_id == "AI_NODE" for f in r.findings)]
        ai_node_counts = [(r.workflow_name, sum(1 for f in r.findings if f.rule_id == "AI_NODE")) for r in ai_workflows]
        ai_node_counts.sort(key=lambda x: -x[1])
        top_ai = ai_node_counts[:5]
        ai_lines = ["Set usage limits and monitoring for AI/API nodes before production."]
        ai_lines.append("  Highest AI exposure:")
        for name, count in top_ai:
            ai_lines.append(f"    - {name}: {pluralize(count, 'AI node')}")
        cost_actions.extend(ai_lines)
    if "HIGH_FAN_OUT" in rule_ids:
        fan_out_workflows = [r for r in result.reports if any(f.rule_id == "HIGH_FAN_OUT" for f in r.findings)]
        names = ", ".join(r.workflow_name for r in fan_out_workflows)
        cost_actions.append(f"Review high fan-out nodes that may cause unexpected API load in {names}.")
    if "MANY_HTTP" in rule_ids:
        http_workflows = [r for r in result.reports if any(f.rule_id == "MANY_HTTP" for f in r.findings)]
        for r in http_workflows:
            ht_nodes = set()
            for f in r.findings:
                if f.rule_id == "MANY_HTTP":
                    ht_nodes.update(f.node_names)
            if ht_nodes:
                node_list = ", ".join(sorted(ht_nodes))
                cost_actions.append(
                    f"Review if all external HTTP calls in '{r.workflow_name}' "
                    f"are necessary ({node_list})."
                )
            else:
                cost_actions.append(f"Review if all external HTTP calls in '{r.workflow_name}' are necessary.")
    if cost_actions:
        for a in cost_actions:
            lines.append(f"- {a}")
    else:
        lines.append("No significant cost control issues identified.")
    lines.append("")

    # Priority 2 — Reliability
    lines.append("## Priority 2 — Reliability")
    lines.append("")
    rel_actions: list[str] = []
    if "NO_ERROR_HANDLING" in rule_ids:
        no_handle_workflows = [r for r in result.reports if any(f.rule_id == "NO_ERROR_HANDLING" for f in r.findings)]
        wf_count = pluralize(len(no_handle_workflows), 'workflow')
        nh_list, nh_remaining = _maybe_truncate(no_handle_workflows, 10)
        rel_actions.append(f"Configure error workflows for the {wf_count} without error handling:")
        for r in nh_list:
            rel_actions.append(f"  - {r.workflow_name}")
        remaining_note = _remaining_note(nh_remaining, "workflows")
        if remaining_note:
            rel_actions.append(f"  {remaining_note}")
    if "WEBHOOK_CHAIN" in rule_ids:
        rel_actions.append("Add idempotency keys and review webhook chain depth to prevent cascading failures.")
    if "DB_IN_LOOP" in rule_ids:
        rel_actions.append("Move database operations outside loops or batch them to avoid performance issues.")
    if result.connection_inventory and result.connection_inventory.isolated_node_names:
        rel_actions.append("Review isolated nodes (no connections) — they may be unused or misconfigured.")
    if rel_actions:
        for a in rel_actions:
            lines.append(f"- {a}")
    else:
        lines.append("No significant reliability issues identified.")
    lines.append("")

    # Priority 3 — Maintainability
    lines.append("## Priority 3 — Maintainability")
    lines.append("")
    maint_actions: list[str] = []
    if "LARGE_WF" in rule_ids:
        maint_actions.append(
            "Split large workflows into smaller, "
            "focused workflows to improve maintainability."
        )
    if result.node_inventory and result.node_inventory.unknown_node_types:
        unk_types = result.node_inventory.unknown_node_types
        unk_list, unk_remaining = _maybe_truncate(list(unk_types), 10)
        unk_msg = f"Review {pluralize(len(unk_types), 'unknown/custom node type')} for compatibility and support"
        if unk_remaining > 0:
            unk_msg += f" (showing {len(unk_list)} of {len(unk_types)})"
        maint_actions.append(f"{unk_msg}:")
        for nt in unk_list:
            maint_actions.append(f"  - `{nt}`")
        remaining_note = _remaining_note(unk_remaining, "types")
        if remaining_note:
            maint_actions.append(f"  {remaining_note}")
    if result.node_inventory and result.node_inventory.disabled_node_count > 0:
        maint_actions.append(
            f"Review {pluralize(result.node_inventory.disabled_node_count, 'disabled node')} "
            "— clean up or re-enable if needed."
        )
    if result.node_inventory and result.node_inventory.credential_reference_count > 0:
        maint_actions.append("Review credential references for governance and rotation policies.")
    if maint_actions:
        for a in maint_actions:
            lines.append(f"- {a}")
    else:
        lines.append("No significant maintainability issues identified.")
    lines.append("")

    # Suggested 7-Day Plan
    lines.append("## Suggested 7-Day Plan")
    lines.append("")
    plan = _generate_7day_plan(result)
    for day, tasks in plan:
        lines.append(f"**{day}:**")
        for t in tasks:
            lines.append(f"- {t}")
        lines.append("")
    lines.append("*Adjust timeline based on workflow criticality and team capacity.*")
    lines.append("")

    # Open Questions For Client
    lines.append("## Open Questions For Client")
    lines.append("")
    questions = _generate_open_questions(result)
    for q in questions:
        lines.append(f"- {q}")
    lines.append("")

    lines.append("---")
    lines.append(f"*Generated by n8n Cost Analyzer v{__version__} — Audit Pack*")
    return "\n".join(lines)


def _generate_7day_plan(result: AnalysisResult) -> list[tuple[str, list[str]]]:
    all_findings = [f for r in result.reports for f in r.findings]
    rule_ids = {f.rule_id for f in all_findings}

    plan: list[tuple[str, list[str]]] = []

    if result.workflow_rankings:
        top_name = result.workflow_rankings[0].workflow_name
        plan.append(("Day 1 — Initial Review", [f"Review top workflow: {top_name}", "Identify production-critical paths"]))
    else:
        plan.append(("Day 1 — Initial Review", ["Review all workflows", "Identify production-critical paths"]))

    day2: list[str] = []
    if "LOOP_HTTP" in rule_ids:
        for r in result.reports:
            if any(f.rule_id == "LOOP_HTTP" for f in r.findings):
                day2.append(f"Add rate limits and concurrency controls around loops in '{r.workflow_name}'")
    if "AI_NODE" in rule_ids:
        day2.append("Set spend limits and monitoring for AI/API nodes")
    if "FREQ_POLL" in rule_ids:
        day2.append("Replace frequent polling with webhook triggers where possible")
    day2.append("Document current trigger configurations")
    plan.append(("Day 2 — Cost Controls", day2))

    day3: list[str] = []
    if "NO_ERROR_HANDLING" in rule_ids:
        no_handle_workflows = [r for r in result.reports if any(f.rule_id == "NO_ERROR_HANDLING" for f in r.findings)]
        names = ", ".join(r.workflow_name for r in no_handle_workflows)
        day3.append(f"Configure error handling for {names}")
    if "WEBHOOK_CHAIN" in rule_ids:
        day3.append("Add idempotency guards to webhook chains")
    if "DB_IN_LOOP" in rule_ids:
        day3.append("Refactor database operations outside loops")
    day3.append("Review retry behavior for HTTP requests")
    plan.append(("Day 3 — Reliability", day3))

    day4: list[str] = []
    if "AI_NODE" in rule_ids:
        day4.append("Estimate token/API costs for AI nodes")
    day4.append("Review external API call volume and pricing")
    day4.append("Add monitoring for execution count per workflow")
    plan.append(("Day 4 — Cost Monitoring", day4))

    day5: list[str] = []
    if result.node_inventory and result.node_inventory.unknown_node_types:
        day5.append("Review unknown/custom node types for compatibility")
    if result.node_inventory and result.node_inventory.disabled_node_count > 0:
        day5.append("Clean up or document disabled nodes")
    if "LARGE_WF" in rule_ids:
        day5.append("Plan splitting large workflows into smaller units")
    day5.append("Document workflow ownership")
    plan.append(("Day 5 — Maintainability", day5))

    day6: list[str] = []
    day6.append("Validate changes in staging environment")
    day6.append("Test error handling paths")
    day6.append("Verify cost controls are working as expected")
    plan.append(("Day 6 — Validation", day6))

    day7: list[str] = []
    day7.append("Document final architecture")
    day7.append("Update runbooks and alerting")
    day7.append("Schedule follow-up audit")
    plan.append(("Day 7 — Documentation & Handover", day7))

    return plan


def _generate_open_questions(result: AnalysisResult) -> list[str]:
    questions: list[str] = []
    questions.append("Which workflows are production-critical and need the highest reliability guarantees?")
    questions.append("What is the acceptable monthly execution volume and budget per workflow?")
    if any(f.rule_id == "AI_NODE" for r in result.reports for f in r.findings):
        questions.append("Which external AI/API services have usage-based pricing and what are the current monthly costs?")
    if any(f.rule_id == "LOOP_HTTP" for r in result.reports for f in r.findings):
        questions.append("What is the typical batch size processed in loop workflows?")
    questions.append("Are any workflows customer-facing or tied to SLAs?")
    if result.node_inventory and result.node_inventory.credential_reference_count > 0:
        questions.append("Who manages credential rotation and what is the current policy?")
    if result.node_inventory and result.node_inventory.unknown_node_types:
        questions.append("Who maintains the custom node types and are they actively supported?")
    questions.append("Who owns each workflow and how is ownership documented?")
    return questions


def write_audit_pack(
    result: AnalysisResult,
    output_dir: str | Path,
    cost_model: CostModel | None = None,
) -> Path:
    p = Path(output_dir)
    p.mkdir(parents=True, exist_ok=True)

    technical = generate_markdown_report(result, cost_model)
    (p / "technical_report.md").write_text(technical, encoding="utf-8")

    executive = generate_executive_summary(result, cost_model)
    (p / "executive_summary.md").write_text(executive, encoding="utf-8")

    action_plan = generate_client_action_plan(result, cost_model)
    (p / "client_action_plan.md").write_text(action_plan, encoding="utf-8")

    write_json_report(result, p / "analysis.json", cost_model)

    return p
