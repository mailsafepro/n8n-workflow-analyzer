from __future__ import annotations

from collections.abc import Sequence

from n8n_cost_analyzer.models import (
    AnalysisResult,
    ConnectionInventory,
    CostModel,
    NodeInventory,
    RiskFinding,
    ScoreSummary,
    WorkflowCostEstimate,
    WorkflowExtraInfo,
    WorkflowRankingEntry,
    WorkflowRiskReport,
)

SEVERITY_POINTS = {
    "low": 5,
    "medium": 15,
    "high": 30,
    "critical": 50,
}


def _cap_score(score: int, maximum: int = 100) -> int:
    return min(score, maximum)


def _compute_scores(findings: Sequence[RiskFinding]) -> dict[str, int]:
    cost_score = 0
    operational_score = 0
    complexity_score = 0
    reliability_score = 0
    security_score = 0

    for f in findings:
        points = SEVERITY_POINTS.get(f.severity, 0)
        cat = f.category
        if cat == "cost":
            cost_score += points
        elif cat == "operational":
            operational_score += points
        elif cat == "complexity":
            complexity_score += points
        elif cat == "reliability":
            reliability_score += points
        elif cat == "security":
            security_score += points

    overall = (
        cost_score * 1
        + operational_score * 1
        + complexity_score * 1
        + reliability_score * 1
        + security_score * 1
    )
    worst = max(cost_score, operational_score, complexity_score, reliability_score, security_score)
    if worst == 0 and overall == 0:
        return {
            "cost_risk_score": 0,
            "operational_risk_score": 0,
            "complexity_score": 0,
            "overall_risk_score": 0,
        }

    return {
        "cost_risk_score": _cap_score(cost_score),
        "operational_risk_score": _cap_score(operational_score),
        "complexity_score": _cap_score(complexity_score),
        "overall_risk_score": _cap_score(overall, maximum=100),
    }


def score_workflow(report: WorkflowRiskReport) -> WorkflowRiskReport:
    scores = _compute_scores(report.findings)
    return WorkflowRiskReport(
        workflow_name=report.workflow_name,
        workflow_id=report.workflow_id,
        active=report.active,
        node_count=report.node_count,
        trigger_types=report.trigger_types,
        findings=report.findings,
        cost_risk_score=scores["cost_risk_score"],
        operational_risk_score=scores["operational_risk_score"],
        complexity_score=scores["complexity_score"],
        overall_risk_score=scores["overall_risk_score"],
    )


def score_analysis(reports: Sequence[WorkflowRiskReport]) -> AnalysisResult:
    scored_reports = tuple(score_workflow(r) for r in reports)
    total_cost = sum(r.cost_risk_score for r in scored_reports)
    total_operational = sum(r.operational_risk_score for r in scored_reports)
    total_complexity = sum(r.complexity_score for r in scored_reports)

    n = len(scored_reports)
    summary = ScoreSummary(
        cost_risk_score=_cap_score(total_cost // max(n, 1)),
        operational_risk_score=_cap_score(total_operational // max(n, 1)),
        complexity_score=_cap_score(total_complexity // max(n, 1)),
        overall_risk_score=_cap_score(
            (total_cost + total_operational + total_complexity) // max(n * 3, 1),
        ),
    )
    return AnalysisResult(
        reports=scored_reports,
        score_summary=summary,
    )


def _cost_risk_label(report: WorkflowRiskReport) -> str:
    if report.overall_risk_score >= 70:
        return "high"
    if report.overall_risk_score >= 40:
        return "medium"
    if report.overall_risk_score > 0:
        return "low"
    return "unknown"


def estimate_workflow_costs(
    result: AnalysisResult,
    cost_model: CostModel | None = None,
) -> tuple[WorkflowCostEstimate, ...]:
    if cost_model is None:
        from n8n_cost_analyzer.cost_model import DEFAULT_COST_MODEL

        cost_model = DEFAULT_COST_MODEL

    estimates: list[WorkflowCostEstimate] = []
    for rpt in result.reports:
        risk_label = _cost_risk_label(rpt)
        drivers: list[str] = []
        notes: list[str] = []
        for f in rpt.findings:
            if f.category == "cost":
                drivers.append(f"{f.rule_id}: {f.message}")

        if risk_label == "high":
            exposure = "significant (heuristic — review manually)"
        elif risk_label == "medium":
            exposure = "moderate (heuristic — review manually)"
        elif risk_label == "low":
            exposure = "minimal (heuristic)"
        else:
            exposure = "unknown"

        if any(f.rule_id == "AI_NODE" for f in rpt.findings):
            notes.append("AI node costs depend on token usage, not execution count")

        estimates.append(WorkflowCostEstimate(
            workflow_name=rpt.workflow_name,
            estimated_cost_risk=risk_label,
            risk_drivers=tuple(drivers),
            estimated_monthly_exposure_label=exposure,
            notes=tuple(notes),
        ))
    return tuple(estimates)


def rank_workflows(result: AnalysisResult) -> tuple[WorkflowRankingEntry, ...]:
    indexed = list(enumerate(result.reports))
    indexed.sort(
        key=lambda x: (
            -x[1].overall_risk_score,
            -sum(1 for f in x[1].findings if f.severity == "critical"),
            -sum(1 for f in x[1].findings if f.severity == "high"),
            -x[1].cost_risk_score,
            x[1].workflow_name,
        ),
    )
    entries: list[WorkflowRankingEntry] = []
    for rank, (_, rpt) in enumerate(indexed, 1):
        top_drivers = list(dict.fromkeys(
            f.rule_id for f in rpt.findings
        ))
        entries.append(WorkflowRankingEntry(
            rank=rank,
            workflow_name=rpt.workflow_name,
            overall_risk_score=rpt.overall_risk_score,
            cost_risk_score=rpt.cost_risk_score,
            finding_count=len(rpt.findings),
            critical_count=sum(1 for f in rpt.findings if f.severity == "critical"),
            high_count=sum(1 for f in rpt.findings if f.severity == "high"),
            top_risk_drivers=tuple(top_drivers),
        ))
    return tuple(entries)


TRIGGER_TYPE_SUFFIXES = ("Trigger", "trigger", "Polling", "polling")


def _is_trigger_type(node_type: str) -> bool:
    return any(node_type.endswith(s) for s in TRIGGER_TYPE_SUFFIXES) or "schedule" in node_type.lower()


def compute_node_inventory(
    reports: Sequence[WorkflowRiskReport],
    workflows_raw: Sequence | None = None,
) -> NodeInventory:
    from n8n_cost_analyzer.node_classifier import classify_node_type

    node_type_counts: dict[str, int] = {}
    node_category_counts: dict[str, int] = {}
    trigger_count = 0
    cred_count = 0
    disabled_count = 0
    unknown_types: set[str] = set()

    if workflows_raw is not None:
        for wf in workflows_raw:
            for node in wf.nodes:
                nt = node.type
                cat = classify_node_type(nt)
                node_type_counts[nt] = node_type_counts.get(nt, 0) + 1
                node_category_counts[cat] = node_category_counts.get(cat, 0) + 1
                if cat == "unknown":
                    unknown_types.add(nt)
                if _is_trigger_type(nt):
                    trigger_count += 1
                if node.credentials is not None:
                    cred_count += 1
                if node.disabled:
                    disabled_count += 1

    return NodeInventory(
        node_type_counts=node_type_counts,
        node_category_counts=node_category_counts,
        trigger_node_count=trigger_count,
        credential_reference_count=cred_count,
        disabled_node_count=disabled_count,
        unknown_node_types=tuple(sorted(unknown_types)),
    )


def compute_connection_inventory(
    reports: Sequence[WorkflowRiskReport],
    workflows_raw: Sequence | None = None,
) -> ConnectionInventory:
    total_edges = 0
    outgoing_map: dict[str, int] = {}
    all_node_names: set[str] = set()
    connected_node_names: set[str] = set()

    if workflows_raw is not None:
        for wf in workflows_raw:
            for node in wf.nodes:
                all_node_names.add(node.name)
            conn = wf.connections or {}
            for source_name, outputs in conn.items():
                all_node_names.add(source_name)
                if isinstance(outputs, dict):
                    for output_arrays in outputs.values():
                        if isinstance(output_arrays, list):
                            for output_index in output_arrays:
                                if isinstance(output_index, list):
                                    for c in output_index:
                                        if isinstance(c, dict):
                                            target = c.get("node", "")
                                            if target:
                                                total_edges += 1
                                                outgoing_map[source_name] = outgoing_map.get(source_name, 0) + 1
                                                connected_node_names.add(source_name)
                                                connected_node_names.add(target)

    high_fan_out = [name for name, count in outgoing_map.items() if count >= 5]
    isolated = sorted(all_node_names - connected_node_names)
    max_out = max(outgoing_map.values()) if outgoing_map else 0

    return ConnectionInventory(
        total_edges=total_edges,
        isolated_node_names=tuple(isolated),
        high_fan_out_nodes=tuple(sorted(high_fan_out)),
        max_outgoing_edges=max_out,
    )


def compute_workflows_extra(
    workflows_raw: Sequence,
) -> tuple[WorkflowExtraInfo, ...]:
    extras: list[WorkflowExtraInfo] = []
    for wf in workflows_raw:
        disabled_count = 0
        cred_count = 0
        type_counts: dict[str, int] = {}
        warnings: list[str] = list(wf.parser_warnings) if hasattr(wf, "parser_warnings") else []
        for node in wf.nodes:
            nt = node.type
            type_counts[nt] = type_counts.get(nt, 0) + 1
            if node.disabled:
                disabled_count += 1
            if node.credentials is not None:
                cred_count += 1
        extras.append(WorkflowExtraInfo(
            disabled_node_count=disabled_count,
            credential_reference_count=cred_count,
            node_type_counts=type_counts,
            parser_warnings=tuple(warnings),
        ))
    return tuple(extras)
