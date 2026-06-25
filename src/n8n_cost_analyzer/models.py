from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class N8nNode:
    id: str | None
    name: str
    type: str
    parameters: dict[str, Any] = field(default_factory=dict)
    position: tuple[float, float] | None = None
    disabled: bool = False
    credentials: dict[str, Any] | None = None
    raw: dict[str, Any] | None = None


@dataclass(frozen=True)
class N8nWorkflow:
    id: str | None
    name: str
    active: bool | None
    nodes: tuple[N8nNode, ...]
    connections: dict[str, Any] = field(default_factory=dict)
    settings: dict[str, Any] = field(default_factory=dict)
    source_path: str | None = None
    tags: tuple[str, ...] = field(default_factory=tuple)
    metadata: dict[str, Any] = field(default_factory=dict)
    parser_warnings: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class RiskFinding:
    rule_id: str
    severity: str  # low, medium, high, critical
    category: str  # cost, operational, complexity, reliability, security
    message: str
    recommendation: str
    workflow_name: str
    node_names: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class WorkflowRiskReport:
    workflow_name: str
    workflow_id: str | None
    active: bool | None
    node_count: int
    trigger_types: tuple[str, ...]
    findings: tuple[RiskFinding, ...]
    cost_risk_score: int = 0
    operational_risk_score: int = 0
    complexity_score: int = 0
    overall_risk_score: int = 0


@dataclass(frozen=True)
class ScoreSummary:
    cost_risk_score: int = 0
    operational_risk_score: int = 0
    complexity_score: int = 0
    overall_risk_score: int = 0


@dataclass(frozen=True)
class CostModel:
    currency: str = "EUR"
    execution_low_cost: float = 0.0001
    execution_medium_cost: float = 0.001
    execution_high_cost: float = 0.01
    ai_node_multiplier: float = 5.0
    http_loop_multiplier: float = 3.0
    polling_multiplier: float = 2.0
    critical_risk_multiplier: float = 4.0


@dataclass(frozen=True)
class WorkflowCostEstimate:
    workflow_name: str
    estimated_cost_risk: str  # low | medium | high | unknown
    risk_drivers: tuple[str, ...] = field(default_factory=tuple)
    estimated_monthly_exposure_label: str = "unknown"
    notes: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class WorkflowRankingEntry:
    rank: int
    workflow_name: str
    overall_risk_score: int
    cost_risk_score: int
    finding_count: int
    critical_count: int
    high_count: int
    top_risk_drivers: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class NodeInventory:
    node_type_counts: dict[str, int] = field(default_factory=dict)
    node_category_counts: dict[str, int] = field(default_factory=dict)
    trigger_node_count: int = 0
    credential_reference_count: int = 0
    disabled_node_count: int = 0
    unknown_node_types: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class ConnectionInventory:
    total_edges: int = 0
    isolated_node_names: tuple[str, ...] = field(default_factory=tuple)
    high_fan_out_nodes: tuple[str, ...] = field(default_factory=tuple)
    max_outgoing_edges: int = 0


@dataclass(frozen=True)
class WorkflowExtraInfo:
    disabled_node_count: int = 0
    credential_reference_count: int = 0
    node_type_counts: dict[str, int] = field(default_factory=dict)
    parser_warnings: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class AnalysisResult:
    reports: tuple[WorkflowRiskReport, ...]
    score_summary: ScoreSummary
    recommendations: tuple[str, ...] = field(default_factory=tuple)
    cost_model: CostModel | None = None
    cost_estimates: tuple[WorkflowCostEstimate, ...] = field(default_factory=tuple)
    workflow_rankings: tuple[WorkflowRankingEntry, ...] = field(default_factory=tuple)
    node_inventory: NodeInventory | None = None
    connection_inventory: ConnectionInventory | None = None
    parser_warnings: tuple[str, ...] = field(default_factory=tuple)
    workflows_extra: tuple[WorkflowExtraInfo, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class CostAssumption:
    label: str
    description: str
    default_value: str
