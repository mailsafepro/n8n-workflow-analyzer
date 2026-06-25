from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from n8n_cost_analyzer.models import AnalysisResult, CostModel
from n8n_cost_analyzer.version import __version__


def _finding_to_dict(finding: Any) -> dict[str, Any]:
    return {
        "rule_id": finding.rule_id,
        "severity": finding.severity,
        "category": finding.category,
        "workflow_name": finding.workflow_name,
        "node_names": list(finding.node_names),
        "message": finding.message,
        "recommendation": finding.recommendation,
    }


def generate_json_report(
    result: AnalysisResult,
    cost_model: CostModel | None = None,
) -> dict[str, Any]:
    s = result.score_summary
    all_findings = [f for r in result.reports for f in r.findings]

    findings_list = [_finding_to_dict(f) for f in all_findings]

    workflow_rankings = []
    for entry in result.workflow_rankings:
        workflow_rankings.append({
            "rank": entry.rank,
            "workflow_name": entry.workflow_name,
            "overall_risk_score": entry.overall_risk_score,
            "cost_risk_score": entry.cost_risk_score,
            "finding_count": entry.finding_count,
            "critical_count": entry.critical_count,
            "high_count": entry.high_count,
            "top_risk_drivers": list(entry.top_risk_drivers),
        })

    cost_model_dict: dict[str, Any] | None = None
    if cost_model is not None:
        cost_model_dict = {
            "currency": cost_model.currency,
            "execution_low_cost": cost_model.execution_low_cost,
            "execution_medium_cost": cost_model.execution_medium_cost,
            "execution_high_cost": cost_model.execution_high_cost,
            "ai_node_multiplier": cost_model.ai_node_multiplier,
            "http_loop_multiplier": cost_model.http_loop_multiplier,
            "polling_multiplier": cost_model.polling_multiplier,
            "critical_risk_multiplier": cost_model.critical_risk_multiplier,
        }

    cost_estimates_list = []
    for ce in result.cost_estimates:
        cost_estimates_list.append({
            "workflow_name": ce.workflow_name,
            "estimated_cost_risk": ce.estimated_cost_risk,
            "risk_drivers": list(ce.risk_drivers),
            "estimated_monthly_exposure_label": ce.estimated_monthly_exposure_label,
            "notes": list(ce.notes),
        })

    # Node inventory
    node_inventory_dict: dict[str, Any] | None = None
    ni = result.node_inventory
    if ni is not None:
        node_inventory_dict = {
            "node_type_counts": dict(ni.node_type_counts),
            "node_category_counts": dict(ni.node_category_counts),
            "trigger_node_count": ni.trigger_node_count,
            "credential_reference_count": ni.credential_reference_count,
            "disabled_node_count": ni.disabled_node_count,
            "unknown_node_types": list(ni.unknown_node_types),
        }

    # Connection inventory
    conn_inventory_dict: dict[str, Any] | None = None
    ci = result.connection_inventory
    if ci is not None:
        conn_inventory_dict = {
            "total_edges": ci.total_edges,
            "isolated_node_names": list(ci.isolated_node_names),
            "high_fan_out_nodes": list(ci.high_fan_out_nodes),
            "max_outgoing_edges": ci.max_outgoing_edges,
        }

    # Workflow-level extra info
    workflows_extra_list = []
    for we in result.workflows_extra:
        workflows_extra_list.append({
            "disabled_node_count": we.disabled_node_count,
            "credential_reference_count": we.credential_reference_count,
            "node_type_counts": dict(we.node_type_counts),
            "parser_warnings": list(we.parser_warnings),
        })

    return {
        "tool": "n8n-cost-analyzer",
        "version": __version__,
        "summary": {
            "workflow_count": len(result.reports),
            "total_findings": len(all_findings),
            "critical_findings": sum(1 for f in all_findings if f.severity == "critical"),
            "high_findings": sum(1 for f in all_findings if f.severity == "high"),
            "overall_risk_score": s.overall_risk_score,
            "cost_risk_score": s.cost_risk_score,
            "operational_risk_score": s.operational_risk_score,
            "complexity_score": s.complexity_score,
        },
        "workflow_rankings": workflow_rankings,
        "findings": findings_list,
        "recommendations": list(result.recommendations),
        "cost_estimates": cost_estimates_list,
        "cost_model": cost_model_dict,
        "parser_warnings": list(result.parser_warnings),
        "node_inventory": node_inventory_dict,
        "connection_inventory": conn_inventory_dict,
        "workflows_extra": workflows_extra_list,
        "assumptions": [
            "Analysis is based on exported JSON workflow definitions only.",
            "Actual execution volume depends on trigger frequency and input data size.",
            "AI/LLM costs are estimated based on node presence, not actual token usage.",
            "HTTP call costs assume external API pricing not included.",
            "Webhook chains are inferred from node types and URL patterns.",
            "Cost estimates are heuristic and not financial quotes.",
            "Credential references are counted; secrets are never exposed.",
            "Disabled nodes are excluded from risk analysis by default.",
        ],
    }


def write_json_report(
    result: AnalysisResult,
    path: str | Path,
    cost_model: CostModel | None = None,
) -> Path:
    p = Path(path)
    data = generate_json_report(result, cost_model)
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    return p
