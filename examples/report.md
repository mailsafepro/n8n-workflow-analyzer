# n8n Workflow Cost & Risk Report

## Audit Summary

- **Overall Risk Score:** 11/100 █░░░░░░░░░
- **Risk Level:** 🟢 Low
- **Workflows analyzed:** 4
- **High-risk workflows:** 3
- **Total findings:** 9 (0 critical, 4 high)
- **Top risk category:** cost
- **Most urgent workflow:** Loop HTTP Workflow

## Executive Summary

- **Cost Risk Score:** 26/100 ██░░░░░░░░
- **Operational Risk Score:** 8/100 ░░░░░░░░░░
- **Complexity Score:** 0/100 ░░░░░░░░░░

## Severity Legend

| Severity | Meaning |
|----------|---------|
| CRITICAL | Immediate attention required. High probability of significant cost overruns or system failure. |
| HIGH | Important risk that should be addressed in the next sprint/cycle. |
| MEDIUM | Notable risk. Monitor and plan mitigation. |
| LOW | Informational. Low probability of material impact. |

## Node Inventory

- **Total unique node types:** 9
- **Trigger nodes:** 1
- **Disabled nodes:** 0
- **Credential references:** 0

| Node Type | Count |
|-----------|-------|
| n8n-nodes-base.httpRequest | 3 |
| n8n-nodes-base.webhook | 2 |
| n8n-nodes-base.set | 2 |
| n8n-nodes-base.cron | 1 |
| n8n-nodes-base.openAi | 1 |
| n8n-nodes-base.splitInBatches | 1 |
| n8n-nodes-base.postgres | 1 |
| n8n-nodes-base.scheduleTrigger | 1 |
| n8n-nodes-base.respondToWebhook | 1 |

## Connection Inventory

- **Total edges:** 9
- **Max outgoing edges:** 2

## Top Workflows To Review First

| Rank | Workflow | Overall Risk | Cost Risk | Critical | High | Top Drivers |
|------|----------|-------------|-----------|----------|------|-------------|
| 1 | Loop HTTP Workflow | 80 | 30 | 0 | 2 | LOOP_HTTP, NO_ERROR_HANDLING, WEBHOOK_CHAIN |
| 2 | AI Workflow | 60 | 45 | 0 | 1 | FREQ_POLL, AI_NODE, NO_ERROR_HANDLING |
| 3 | Polling Workflow | 45 | 30 | 0 | 1 | FREQ_POLL, NO_ERROR_HANDLING |
| 4 | Simple Webhook Workflow | 0 | 0 | 0 | 0 | — |

## Workflow Inventory

| # | Workflow | Active | Nodes | Triggers | Risk Score |
|---|----------|--------|-------|----------|------------|
| 1 | AI Workflow | ✅ | 3 | none | 60 |
| 2 | Loop HTTP Workflow | ✅ | 4 | none | 80 |
| 3 | Polling Workflow | ✅ | 3 | n8n-nodes-base.scheduleTrigger | 45 |
| 4 | Simple Webhook Workflow | ✅ | 3 | none | 0 |

## Quick Wins

1. Replace frequent polling with webhook/event-based triggers to reduce execution volume and cost.
2. Estimate token/API cost before moving AI nodes to production. Set usage limits and monitor spend regularly.
3. Configure error workflow/handling on critical workflows to ensure failures are caught and notified.
4. Add guardrails, rate limits, and concurrency controls around loops with HTTP to prevent runaway API costs.
5. Review webhook chain depth and add idempotency keys to prevent duplicate processing.

## Top Risks

| Severity | Category | Workflow | Message |
|----------|----------|----------|---------|
| HIGH | cost | AI Workflow | Frequent polling trigger 'Cron' can create high execution volume |
| HIGH | cost | Loop HTTP Workflow | HTTP Request node inside a loop/batch can multiply API calls and costs |
| HIGH | operational | Loop HTTP Workflow | Database operation inside a loop can cause performance issues and unexpected costs |
| HIGH | cost | Polling Workflow | Frequent polling trigger 'Schedule' can create high execution volume |
| MEDIUM | cost | AI Workflow | AI/LLM node 'OpenAI' has variable token-based cost that can escalate |
| MEDIUM | reliability | AI Workflow | Workflow has no error workflow configured |
| MEDIUM | reliability | Loop HTTP Workflow | Workflow has no error workflow configured |
| MEDIUM | reliability | Polling Workflow | Workflow has no error workflow configured |
| LOW | operational | Loop HTTP Workflow | Webhook 'Webhook' triggers external HTTP calls — cascading chain risk |

## Cost Risk Findings

| Severity | Workflow | Node(s) | Finding |
|----------|----------|---------|---------|
| HIGH | AI Workflow | Cron | Frequent polling trigger 'Cron' can create high execution volume |
| MEDIUM | AI Workflow | OpenAI | AI/LLM node 'OpenAI' has variable token-based cost that can escalate |
| HIGH | Loop HTTP Workflow | Split In Batches, HTTP Request per item | HTTP Request node inside a loop/batch can multiply API calls and costs |
| HIGH | Polling Workflow | Schedule | Frequent polling trigger 'Schedule' can create high execution volume |

## Estimated Cost Exposure

- **AI Workflow:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: FREQ_POLL: Frequent polling trigger 'Cron' can create high execution volume
  - Driver: AI_NODE: AI/LLM node 'OpenAI' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Loop HTTP Workflow:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
- **Polling Workflow:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: FREQ_POLL: Frequent polling trigger 'Schedule' can create high execution volume
- **Simple Webhook Workflow:** ⚪ UNKNOWN — unknown

*Cost estimates are heuristic — based on static analysis, not actual financial quotes.*

## Operational Risk Findings

| Severity | Workflow | Node(s) | Finding |
|----------|----------|---------|---------|
| LOW | Loop HTTP Workflow | Webhook | Webhook 'Webhook' triggers external HTTP calls — cascading chain risk |
| HIGH | Loop HTTP Workflow | Split In Batches, Postgres | Database operation inside a loop can cause performance issues and unexpected costs |

## Complexity Findings

No complexity findings.

## Recommendations

1. Replace frequent polling with webhook/event-based triggers to reduce execution volume and cost.
2. Estimate token/API cost before moving AI nodes to production. Set usage limits and monitor spend regularly.
3. Configure error workflow/handling on critical workflows to ensure failures are caught and notified.
4. Add guardrails, rate limits, and concurrency controls around loops with HTTP to prevent runaway API costs.
5. Review webhook chain depth and add idempotency keys to prevent duplicate processing.
6. Move database operations outside loops or batch them to avoid performance degradation and unexpected costs.

## Workflow-Level Details

### AI Workflow

- **ID:** 4
- **Active:** True
- **Nodes:** 3
- **Triggers:** none
- **Scores:** Cost=45 | Ops=0 | Complexity=0 | Overall=60

**Findings:**
  - [HIGH] [cost] FREQ_POLL: Frequent polling trigger 'Cron' can create high execution volume
    - Nodes: Cron
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'OpenAI' has variable token-based cost that can escalate
    - Nodes: OpenAI
  - [MEDIUM] [reliability] NO_ERROR_HANDLING: Workflow has no error workflow configured

### Loop HTTP Workflow

- **ID:** 3
- **Active:** True
- **Nodes:** 4
- **Triggers:** none
- **Scores:** Cost=30 | Ops=35 | Complexity=0 | Overall=80

**Findings:**
  - [HIGH] [cost] LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
    - Nodes: Split In Batches, HTTP Request per item
  - [MEDIUM] [reliability] NO_ERROR_HANDLING: Workflow has no error workflow configured
  - [LOW] [operational] WEBHOOK_CHAIN: Webhook 'Webhook' triggers external HTTP calls — cascading chain risk
    - Nodes: Webhook
  - [HIGH] [operational] DB_IN_LOOP: Database operation inside a loop can cause performance issues and unexpected costs
    - Nodes: Split In Batches, Postgres

### Polling Workflow

- **ID:** 2
- **Active:** True
- **Nodes:** 3
- **Triggers:** n8n-nodes-base.scheduleTrigger
- **Scores:** Cost=30 | Ops=0 | Complexity=0 | Overall=45

**Findings:**
  - [HIGH] [cost] FREQ_POLL: Frequent polling trigger 'Schedule' can create high execution volume
    - Nodes: Schedule
  - [MEDIUM] [reliability] NO_ERROR_HANDLING: Workflow has no error workflow configured

### Simple Webhook Workflow

- **ID:** 1
- **Active:** True
- **Nodes:** 3
- **Triggers:** none
- **Scores:** Cost=0 | Ops=0 | Complexity=0 | Overall=0

## Workflow Risk Ranking

| Rank | Workflow | Overall | Cost | Ops | Complexity | Findings |
|------|----------|---------|------|-----|------------|----------|
| 1 | Loop HTTP Workflow | 80 | 30 | 35 | 0 | 4 |
| 2 | AI Workflow | 60 | 45 | 0 | 0 | 3 |
| 3 | Polling Workflow | 45 | 30 | 0 | 0 | 2 |
| 4 | Simple Webhook Workflow | 0 | 0 | 0 | 0 | 0 |

## Assumptions

- Analysis is based on exported JSON workflow definitions only.
- Actual execution volume depends on trigger frequency and input data size.
- AI/LLM costs are estimated based on node presence, not actual token usage.
- HTTP call costs assume external API pricing not included.
- Webhook chains are inferred from node types and URL patterns.
- Cost estimates are heuristic and not financial quotes.
- Credential references are counted; secrets are never exposed.
- Disabled nodes are excluded from risk analysis by default.

## Appendix

### Rule Reference

| Rule ID | Description | Default Severity | Category |
|---------|-------------|------------------|----------|
| FREQ_POLL | Frequent polling/schedule trigger | high | cost |
| LOOP_HTTP | Loop/batch combined with HTTP request | high | cost |
| AI_NODE | AI/LLM node detected | medium | cost |
| LARGE_WF | Workflow with many nodes | medium/critical | complexity |
| NO_ERROR_HANDLING | Missing error workflow | medium | reliability |
| WEBHOOK_CHAIN | Webhook chaining to internal URLs | medium/low | operational |
| DB_IN_LOOP | Database operation inside loop | high | operational |
| MANY_HTTP | Multiple HTTP Request nodes | low | cost |
| HIGH_FAN_OUT | Node with 5+ outgoing connections | medium | complexity |

---
*Generated by n8n Cost Analyzer v0.3.0*