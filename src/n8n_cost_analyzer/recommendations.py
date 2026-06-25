from __future__ import annotations

from collections.abc import Sequence

from n8n_cost_analyzer.models import RiskFinding

RECOMMENDATION_MAP: dict[str, str] = {
    "FREQ_POLL": "Replace frequent polling with webhook/event-based triggers to reduce execution volume and cost.",
    "LOOP_HTTP": "Add guardrails, rate limits, and concurrency controls around loops with HTTP to prevent runaway API costs.",
    "AI_NODE": "Estimate token/API cost before moving AI nodes to production. Set usage limits and monitor spend regularly.",
    "LARGE_WF": "Split large workflows into smaller focused workflows to improve maintainability and reduce blast radius.",
    "NO_ERROR_HANDLING": "Configure error workflow/handling on critical workflows to ensure failures are caught and notified.",
    "WEBHOOK_CHAIN": "Review webhook chain depth and add idempotency keys to prevent duplicate processing.",
    "DB_IN_LOOP": "Move database operations outside loops or batch them to avoid performance degradation and unexpected costs.",
    "MANY_HTTP": "Review if all external HTTP calls are necessary. Consider caching or batching to reduce dependency costs.",
}


def generate_recommendations(findings: Sequence[RiskFinding]) -> tuple[str, ...]:
    seen: set[str] = set()
    recommendations: list[str] = []
    for f in findings:
        rec = RECOMMENDATION_MAP.get(f.rule_id)
        if rec and rec not in seen:
            seen.add(rec)
            recommendations.append(rec)
    return tuple(recommendations)
