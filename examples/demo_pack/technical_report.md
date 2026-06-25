# n8n Workflow Cost & Risk Report

## How to Read This Report

If you only have a few minutes, start with these sections:

1. **Audit Summary** — overall risk scores at a glance
2. **Top Workflows To Review First** — ranked by risk
3. **Workflow Summaries** — one-line narrative per workflow
4. **Quick Wins** — immediate actions with the most impact

For a deeper review, read the full report in order.

## Audit Summary

- **Overall Risk Score:** 5/100 ░░░░░░░░░░
- **Risk Level:** 🟢 Low
- **Workflows analyzed:** 12 workflows
- **High-risk workflows:** 4
- **Total findings:** 16 findings (0 criticals, 5 highs)
- **Top risk category:** cost
- **Most urgent workflow:** Loop HTTP Workflow
- **Parser warnings:** 2 warnings

## Parser Warnings

- ⚠ Unknown node type 'n8n-nodes-base.myCustomNode' in node 'My Custom Node'
- ⚠ Unknown node type 'com.legacy.connector' in node 'Legacy Connector'

## Executive Summary

- **Cost Risk Score:** 12/100 █░░░░░░░░░
- **Operational Risk Score:** 3/100 ░░░░░░░░░░
- **Complexity Score:** 1/100 ░░░░░░░░░░

> **Note:** 2 community/custom node types found. These may have cost or
> risk profiles not covered by built-in rules. See the Community/Custom section for details.

## How to Interpret Risk Scores

Risk scores are a relative indicator, not an absolute measure:

| Range | Meaning |
|-------|---------|
| 0 | No risks detected |
| 1–20 | Low risk — maintain current practices |
| 21–40 | Moderate risk — monitor and plan mitigation |
| 41–70 | Review recommended — address in the next cycle |
| 71–100 | High priority — take immediate action |

**Important:** The portfolio-level score (e.g., 12/100) can be low even if individual
workflows have high scores. Always check the workflow rankings and per-workflow
details to identify the most urgent items.

## Severity Legend

| Severity | Meaning |
|----------|---------|
| CRITICAL | Immediate attention required. High probability of significant cost overruns or system failure. |
| HIGH | Important risk that should be addressed in the next sprint/cycle. |
| MEDIUM | Notable risk. Monitor and plan mitigation. |
| LOW | Informational. Low probability of material impact. |

## Workflow Summaries

| Workflow | Priority | Narrative | Next Action |
|----------|----------|-----------|-------------|
| AI Workflow | Review recommended (60) | Has AI/LLM nodes with variable token-based costs; uses frequent polling which can drive high execution volume; lacks error handling for failure scenarios. | Estimate and monitor costs before production |
| Collection Workflow One | Low (0) | No significant risks detected. | Review and assess |
| Collection Workflow Two | Low (0) | No significant risks detected. | Review and assess |
| High Fan-Out Workflow | Review recommended (40) | Lacks error handling for failure scenarios; has a high fan-out node that may cause unexpected API load; makes many external HTTP calls; chains webhook triggers which can cascade unexpectedly. | Configure error workflow |
| Loop HTTP Workflow | High priority (80) | Combines HTTP calls inside loop or batch logic, creating a runaway execution risk; lacks error handling for failure scenarios; runs database operations inside loops, risking performance issues; chains webhook triggers which can cascade unexpectedly. | Add rate limits and concurrency controls |
| Polling Workflow | Review recommended (45) | Uses frequent polling which can drive high execution volume; lacks error handling for failure scenarios. | Estimate and monitor costs before production |
| Simple Webhook Workflow | Low (0) | No significant risks detected. | Review and assess |
| Workflow with Unknown Nodes | Low (0) | No significant risks detected. | Review and assess |
| Workflow with Credentials | Low (0) | No significant risks detected. | Review and assess |
| Workflow with Disabled Nodes | Moderate (30) | Uses frequent polling which can drive high execution volume. | Review and assess |
| Data Wrapped Workflow One | Low (15) | Lacks error handling for failure scenarios. | Configure error workflow |
| Data Wrapped Workflow Two | Low (15) | Has AI/LLM nodes with variable token-based costs. | Review and assess |

## Node Inventory

- **Total unique node types:** 13 types
- **Trigger nodes:** 3 nodes
- **Disabled nodes:** 2 nodes
- **Credential references:** 2 references
- **Unknown node types:** 2 types

### Node Categories

| Category | Count |
|----------|-------|
| trigger | 13 |
| http_api | 9 |
| transform | 8 |
| ai | 3 |
| database | 2 |
| unknown | 2 |
| control_flow | 1 |
| communication | 1 |

### Node Types

| Node Type | Count |
|-----------|-------|
| n8n-nodes-base.httpRequest | 9 |
| n8n-nodes-base.webhook | 7 |
| n8n-nodes-base.set | 6 |
| n8n-nodes-base.openAi | 3 |
| n8n-nodes-base.scheduleTrigger | 3 |
| n8n-nodes-base.cron | 2 |
| n8n-nodes-base.noOp | 2 |
| n8n-nodes-base.postgres | 2 |
| n8n-nodes-base.splitInBatches | 1 |
| n8n-nodes-base.respondToWebhook | 1 |
| n8n-nodes-base.myCustomNode | 1 |
| com.legacy.connector | 1 |
| n8n-nodes-base.slack | 1 |

## Community / Custom / Unclassified Node Types

The following 2 node types are from community packages, custom builds,
or unrecognized sources.
They may have custom cost or risk profiles not covered by built-in rules:

- `com.legacy.connector`
- `n8n-nodes-base.myCustomNode`

## Connection Inventory

- **Total edges:** 27
- **Max outgoing edges:** 6
- **High fan-out nodes:** Branch Node, Webhook

## Top Workflows To Review First

| Rank | Workflow | Overall Risk | Cost Risk | Critical | High | Top Drivers |
|------|----------|-------------|-----------|----------|------|-------------|
| 1 | Loop HTTP Workflow | 80 | 30 | 0 | 2 | LOOP_HTTP, NO_ERROR_HANDLING, WEBHOOK_CHAIN |
| 2 | AI Workflow | 60 | 45 | 0 | 1 | FREQ_POLL, AI_NODE, NO_ERROR_HANDLING |
| 3 | Polling Workflow | 45 | 30 | 0 | 1 | FREQ_POLL, NO_ERROR_HANDLING |
| 4 | High Fan-Out Workflow | 40 | 5 | 0 | 0 | NO_ERROR_HANDLING, WEBHOOK_CHAIN, MANY_HTTP |
| 5 | Workflow with Disabled Nodes | 30 | 30 | 0 | 1 | FREQ_POLL |
| 6 | Data Wrapped Workflow Two | 15 | 15 | 0 | 0 | AI_NODE |
| 7 | Data Wrapped Workflow One | 15 | 0 | 0 | 0 | NO_ERROR_HANDLING |
| 8 | Collection Workflow One | 0 | 0 | 0 | 0 | — |
| 9 | Collection Workflow Two | 0 | 0 | 0 | 0 | — |
| 10 | Simple Webhook Workflow | 0 | 0 | 0 | 0 | — |
| 11 | Workflow with Credentials | 0 | 0 | 0 | 0 | — |
| 12 | Workflow with Unknown Nodes | 0 | 0 | 0 | 0 | — |

## Workflow Inventory

| # | Workflow | Active | Nodes | Triggers | Risk Score |
|---|----------|--------|-------|----------|------------|
| 1 | AI Workflow | ✅ | 3 | none | 60 |
| 2 | Collection Workflow One | ✅ | 2 | none | 0 |
| 3 | Collection Workflow Two | ❌ | 2 | n8n-nodes-base.scheduleTrigger | 0 |
| 4 | High Fan-Out Workflow | ✅ | 7 | none | 40 |
| 5 | Loop HTTP Workflow | ✅ | 4 | none | 80 |
| 6 | Polling Workflow | ✅ | 3 | n8n-nodes-base.scheduleTrigger | 45 |
| 7 | Simple Webhook Workflow | ✅ | 3 | none | 0 |
| 8 | Workflow with Unknown Nodes | ✅ | 4 | none | 0 |
| 9 | Workflow with Credentials | ✅ | 3 | none | 0 |
| 10 | Workflow with Disabled Nodes | ✅ | 4 | n8n-nodes-base.scheduleTrigger | 30 |
| 11 | Data Wrapped Workflow One | ✅ | 2 | none | 15 |
| 12 | Data Wrapped Workflow Two | ✅ | 2 | none | 15 |

## Quick Wins

1. Add rate limits and concurrency controls around the HTTP loop in 'Loop HTTP Workflow'.
2. Configure error workflow handling in 5 workflows.
3. Replace frequent polling with webhook/event-based triggers to reduce execution volume and cost.
4. Estimate token/API cost before moving AI nodes to production. Set usage limits and monitor spend regularly.
5. Review webhook chain depth and add idempotency keys to prevent duplicate processing.

## Top Risks

| Severity | Category | Workflow | Message |
|----------|----------|----------|---------|
| HIGH | cost | AI Workflow | Frequent polling trigger 'Cron' can create high execution volume |
| HIGH | cost | Loop HTTP Workflow | HTTP Request node inside a loop/batch can multiply API calls and costs |
| HIGH | operational | Loop HTTP Workflow | Database operation inside a loop can cause performance issues and unexpected costs |
| HIGH | cost | Polling Workflow | Frequent polling trigger 'Schedule' can create high execution volume |
| HIGH | cost | Workflow with Disabled Nodes | Frequent polling trigger 'Schedule' can create high execution volume |
| MEDIUM | cost | AI Workflow | AI/LLM node 'OpenAI' has variable token-based cost that can escalate |
| MEDIUM | reliability | AI Workflow | Workflow has no error workflow configured |
| MEDIUM | reliability | High Fan-Out Workflow | Workflow has no error workflow configured |
| MEDIUM | complexity | High Fan-Out Workflow | Node 'Branch Node' has 5 outgoing connections (high fan-out) |
| MEDIUM | reliability | Loop HTTP Workflow | Workflow has no error workflow configured |

## Cost Risk Findings

| Severity | Workflow | Node(s) | Finding |
|----------|----------|---------|---------|
| HIGH | AI Workflow | Cron | Frequent polling trigger 'Cron' can create high execution volume |
| MEDIUM | AI Workflow | OpenAI | AI/LLM node 'OpenAI' has variable token-based cost that can escalate |
| LOW | High Fan-Out Workflow | Target A, Target B, Target C, Target D | Workflow has 4 HTTP Request nodes, increasing external dependency and cost |
| HIGH | Loop HTTP Workflow | Split In Batches, HTTP Request per item | HTTP Request node inside a loop/batch can multiply API calls and costs |
| HIGH | Polling Workflow | Schedule | Frequent polling trigger 'Schedule' can create high execution volume |
| HIGH | Workflow with Disabled Nodes | Schedule | Frequent polling trigger 'Schedule' can create high execution volume |
| MEDIUM | Data Wrapped Workflow Two | OpenAI Call | AI/LLM node 'OpenAI Call' has variable token-based cost that can escalate |

## Estimated Cost Exposure

- **AI Workflow:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: FREQ_POLL: Frequent polling trigger 'Cron' can create high execution volume
  - Driver: AI_NODE: AI/LLM node 'OpenAI' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Collection Workflow One:** ⚪ UNKNOWN — unknown
- **Collection Workflow Two:** ⚪ UNKNOWN — unknown
- **High Fan-Out Workflow:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: MANY_HTTP: Workflow has 4 HTTP Request nodes, increasing external dependency and cost
- **Loop HTTP Workflow:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
- **Polling Workflow:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: FREQ_POLL: Frequent polling trigger 'Schedule' can create high execution volume
- **Simple Webhook Workflow:** ⚪ UNKNOWN — unknown
- **Workflow with Unknown Nodes:** ⚪ UNKNOWN — unknown
- **Workflow with Credentials:** ⚪ UNKNOWN — unknown
- **Workflow with Disabled Nodes:** 🟢 LOW — minimal (heuristic)
  - Driver: FREQ_POLL: Frequent polling trigger 'Schedule' can create high execution volume
- **Data Wrapped Workflow One:** 🟢 LOW — minimal (heuristic)
- **Data Wrapped Workflow Two:** 🟢 LOW — minimal (heuristic)
  - Driver: AI_NODE: AI/LLM node 'OpenAI Call' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count

*Cost estimates are heuristic — based on static analysis, not actual financial quotes.*

## Operational Risk Findings

| Severity | Workflow | Node(s) | Finding |
|----------|----------|---------|---------|
| LOW | High Fan-Out Workflow | Webhook | Webhook 'Webhook' triggers external HTTP calls — cascading chain risk |
| LOW | Loop HTTP Workflow | Webhook | Webhook 'Webhook' triggers external HTTP calls — cascading chain risk |
| HIGH | Loop HTTP Workflow | Split In Batches, Postgres | Database operation inside a loop can cause performance issues and unexpected costs |

## Complexity Findings

| Severity | Workflow | Finding |
|----------|----------|---------|
| MEDIUM | High Fan-Out Workflow | Node 'Branch Node' has 5 outgoing connections (high fan-out) |

## Recommendations

1. Replace frequent polling with webhook/event-based triggers to reduce execution volume and cost.
2. Estimate token/API cost before moving AI nodes to production. Set usage limits and monitor spend regularly.
3. Configure error workflow/handling on critical workflows to ensure failures are caught and notified.
4. Review webhook chain depth and add idempotency keys to prevent duplicate processing.
5. Review if all external HTTP calls are necessary. Consider caching or batching to reduce dependency costs.
6. Add guardrails, rate limits, and concurrency controls around loops with HTTP to prevent runaway API costs.
7. Move database operations outside loops or batch them to avoid performance degradation and unexpected costs.

## Workflow-Level Details

### AI Workflow

- **ID:** 4
- **Active:** ✅
- **Nodes:** 3
- **Triggers:** none
- **Scores:** Cost=45 | Ops=0 | Complexity=0 | Overall=60

**Findings:**
  - [HIGH] [cost] FREQ_POLL: Frequent polling trigger 'Cron' can create high execution volume
    - Nodes: Cron
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'OpenAI' has variable token-based cost that can escalate
    - Nodes: OpenAI
  - [MEDIUM] [reliability] NO_ERROR_HANDLING: Workflow has no error workflow configured

### Collection Workflow One

- **ID:** wf-1
- **Active:** ✅
- **Nodes:** 2
- **Triggers:** none
- **Scores:** Cost=0 | Ops=0 | Complexity=0 | Overall=0

### Collection Workflow Two

- **ID:** wf-2
- **Active:** ❌
- **Nodes:** 2
- **Triggers:** n8n-nodes-base.scheduleTrigger
- **Scores:** Cost=0 | Ops=0 | Complexity=0 | Overall=0

### High Fan-Out Workflow

- **ID:** wf-fanout
- **Active:** ✅
- **Nodes:** 7
- **Triggers:** none
- **Scores:** Cost=5 | Ops=5 | Complexity=15 | Overall=40

**Findings:**
  - [MEDIUM] [reliability] NO_ERROR_HANDLING: Workflow has no error workflow configured
  - [LOW] [operational] WEBHOOK_CHAIN: Webhook 'Webhook' triggers external HTTP calls — cascading chain risk
    - Nodes: Webhook
  - [LOW] [cost] MANY_HTTP: Workflow has 4 HTTP Request nodes, increasing external dependency and cost
    - Nodes: Target A, Target B, Target C, Target D
  - [MEDIUM] [complexity] HIGH_FAN_OUT: Node 'Branch Node' has 5 outgoing connections (high fan-out)
    - Nodes: Branch Node

### Loop HTTP Workflow

- **ID:** 3
- **Active:** ✅
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
- **Active:** ✅
- **Nodes:** 3
- **Triggers:** n8n-nodes-base.scheduleTrigger
- **Scores:** Cost=30 | Ops=0 | Complexity=0 | Overall=45

**Findings:**
  - [HIGH] [cost] FREQ_POLL: Frequent polling trigger 'Schedule' can create high execution volume
    - Nodes: Schedule
  - [MEDIUM] [reliability] NO_ERROR_HANDLING: Workflow has no error workflow configured

### Simple Webhook Workflow

- **ID:** 1
- **Active:** ✅
- **Nodes:** 3
- **Triggers:** none
- **Scores:** Cost=0 | Ops=0 | Complexity=0 | Overall=0

### Workflow with Unknown Nodes

- **ID:** wf-unknown
- **Active:** ✅
- **Nodes:** 4
- **Triggers:** none
- **Scores:** Cost=0 | Ops=0 | Complexity=0 | Overall=0

### Workflow with Credentials

- **ID:** wf-cred
- **Active:** ✅
- **Nodes:** 3
- **Triggers:** none
- **Scores:** Cost=0 | Ops=0 | Complexity=0 | Overall=0

### Workflow with Disabled Nodes

- **ID:** wf-disabled
- **Active:** ✅
- **Nodes:** 4
- **Triggers:** n8n-nodes-base.scheduleTrigger
- **Scores:** Cost=30 | Ops=0 | Complexity=0 | Overall=30

**Findings:**
  - [HIGH] [cost] FREQ_POLL: Frequent polling trigger 'Schedule' can create high execution volume
    - Nodes: Schedule

*... and 2 more workflows with hidden details (table truncated for readability)*

## Workflow Risk Ranking

| Rank | Workflow | Overall | Cost | Ops | Complexity | Findings |
|------|----------|---------|------|-----|------------|----------|
| 1 | Loop HTTP Workflow | 80 | 30 | 35 | 0 | 4 |
| 2 | AI Workflow | 60 | 45 | 0 | 0 | 3 |
| 3 | Polling Workflow | 45 | 30 | 0 | 0 | 2 |
| 4 | High Fan-Out Workflow | 40 | 5 | 5 | 15 | 4 |
| 5 | Workflow with Disabled Nodes | 30 | 30 | 0 | 0 | 1 |
| 6 | Data Wrapped Workflow Two | 15 | 15 | 0 | 0 | 1 |
| 7 | Data Wrapped Workflow One | 15 | 0 | 0 | 0 | 1 |
| 8 | Collection Workflow One | 0 | 0 | 0 | 0 | 0 |
| 9 | Collection Workflow Two | 0 | 0 | 0 | 0 | 0 |
| 10 | Simple Webhook Workflow | 0 | 0 | 0 | 0 | 0 |
| 11 | Workflow with Credentials | 0 | 0 | 0 | 0 | 0 |
| 12 | Workflow with Unknown Nodes | 0 | 0 | 0 | 0 | 0 |

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
*Generated by n8n Cost Analyzer v0.7.1*