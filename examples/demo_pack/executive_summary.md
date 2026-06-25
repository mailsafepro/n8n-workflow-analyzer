# Executive Summary — n8n Workflow Cost & Risk Audit

## How to Read This Report

Start with **Overall Assessment** for a quick score overview.
Then **Portfolio Insights** and **Top Risk Patterns** for what matters most.
Use **Top Workflows To Review** for specific remediation targets.
The **What To Do First** section provides concrete next steps.

## Overall Assessment

- **Workflows analyzed:** 12 workflows
- **Overall portfolio risk:** 🟢 Low (5/100)
- **Cost risk:** 🟢 Low (12/100)
- **Operational / reliability risk:** 🟢 Low (3/100)
- **Complexity risk:** 🟢 Low (1/100)
- **Total findings:** 16 findings (5 high findings, 8 medium findings, 3 low findings)
- **Most urgent workflow:** Loop HTTP Workflow

## Portfolio Insights

- ~17% of workflows (2/12) contain AI/API nodes with variable token-based costs.
- ~42% of workflows (5/12) lack error handling — silent failures are likely.
- A small subset (top 5 workflows) concentrates ~88% of all findings (14/16).
- Average of ~1.3 findings per workflow.
- 4 workflows have review-worthy risk patterns (score ≥ 40); the rest are low or zero risk.

**Interpretation:**
Risk is unevenly distributed — remediation can focus on a subset of workflows and patterns rather than the entire portfolio.

## Top Risk Patterns Detected

1. **Missing error handling** — 5 workflows
   → Caused by: NO_ERROR_HANDLING — no error workflow configured
   → Impact: Silent failures, undetected outages, and potential data loss on execution errors

2. **AI/API cost exposure** — 2 workflows, 2 occurrences
   → Caused by: AI_NODE — AI/LLM nodes with token-based pricing
   → Impact: Variable and potentially unbounded costs per workflow execution; cost scales with input complexity and volume

3. **High external API usage** — 2 workflows, 2 occurrences
   → Caused by: MANY_HTTP / LOOP_HTTP — multiple HTTP nodes or loops containing HTTP calls
   → Impact: Cost, latency, and external dependency risk; loops can amplify API usage multiplicatively

4. **Loop-based scaling risks** — 1 workflow, 1 occurrence
   → Caused by: LOOP_HTTP — HTTP requests inside loop or batch logic
   → Impact: Multiplicative execution cost; batch size directly multiplies API calls and LLM tokens

5. **Large or complex workflows** — 1 workflow, 1 occurrence
   → Caused by: LARGE_WF / HIGH_FAN_OUT — oversized workflows or excessive branching
   → Impact: Reduced maintainability, harder debugging, and unexpected API load from fan-out nodes

## Top Workflows To Review

| # | Workflow | Review Priority | Risk Drivers | Concentration | Suggested Action |
|---|----------|-----------------|--------------|---------------|------------------|
| 1 | Loop HTTP Workflow | High priority | LOOP_HTTP, NO_ERROR_HANDLING, WEBHOOK_CHAIN | High | Add rate limits and guards |
| 2 | AI Workflow | Review recommended | FREQ_POLL, AI_NODE, NO_ERROR_HANDLING | High | Replace polling with webhooks |
| 3 | Polling Workflow | Review recommended | FREQ_POLL, NO_ERROR_HANDLING | Medium | Replace polling with webhooks |
| 4 | High Fan-Out Workflow | Review recommended | NO_ERROR_HANDLING, WEBHOOK_CHAIN, MANY_HTTP | High | Configure error workflow |
| 5 | Workflow with Disabled Nodes | Moderate | FREQ_POLL | Medium | Replace polling with webhooks |

## Cost Exposure Overview

- 2 workflows contain AI/API cost-sensitive nodes.
- 3 workflows use high-frequency triggers or polling patterns.
- 1 workflow contains loop + HTTP combinations — multiplicative execution cost.
- 1 workflow has multiple external HTTP calls, increasing dependency costs.

AI/API nodes represent variable cost, while loops and polling can amplify execution count. Together, these create the highest cost uncertainty in the portfolio.

## Credential Footprint

- **Total credential references:** 2
- **Average per workflow:** ~0.2
- **Highest concentration:** Workflow with Credentials (2 references)
- **Custom/community node types:** 2 — may have unknown credential patterns

Credential references are present but not widespread in this export.
This increases the importance of:
- proper credential scoping and rotation policies
- avoiding reuse across unrelated workflows
- auditing custom node credential handling

## Business Impact

### Cost Risk
- AI/API usage introduces variable and hard-to-predict costs across 2 workflows.
- Loop + HTTP patterns can multiply API usage unexpectedly in 1 workflow.
- 1 workflow makes many external HTTP calls, increasing dependency costs.

### Reliability Risk
- 5 workflows lack error handling — silent failures may go undetected.
- 2 workflows with webhook chains — cascading failure risk.
- 1 workflow runs database operations in loops — risk of performance degradation.

### Operational Complexity
- 1 workflow has high fan-out nodes, increasing debugging difficulty.
- 2 custom/community node types introduce dependency and compatibility risk.

### Governance
- 2 credential references across all workflows suggest need for governance.
- Credential reuse and rotation policies should be reviewed.
- Workflow ownership and credential scoping should be documented.
- 2 custom node types — verify support status and credential handling.

## What To Do First

1. Review the top 3 highest-risk workflows first — add rate limits to loop + HTTP patterns (Loop HTTP Workflow, AI Workflow, Polling Workflow).
2. Add error handling to 5 workflows currently without it.
3. Set usage limits and monitoring on AI/API nodes in 2 workflows.
4. Inspect loop + HTTP combinations in 1 workflow for cost amplification risk.
5. Review credential usage across the portfolio — identify ownership and rotation needs.

## Recommended Next Step

> Prioritize high-risk workflows for review in the next sprint.

## How to Interpret Risk Scores

Risk scores are a relative indicator, not an absolute measure:

| Range | Meaning |
|-------|---------|
| 0 | No risks detected |
| 1–20 | Low risk — maintain current practices |
| 21–40 | Moderate risk — monitor and plan mitigation |
| 41–70 | Review recommended — address in the next cycle |
| 71–100 | High priority — take immediate action |

The portfolio score can be low even if individual workflows have high scores.
Always check the workflow rankings for the most urgent items.

## Caveats

This analysis is based on static workflow definitions only. The following limitations apply:

- Heuristic analysis based on node types and patterns, not actual execution data.
- Cost estimates are approximate and derived from configurable assumptions.
- No runtime metrics, execution logs, or production monitoring data were used.
- No credentials or secrets were inspected.
- Actual costs depend on trigger frequency, input data volume, and external API pricing.

---
*Generated by n8n Cost Analyzer v0.7.1 — Audit Pack*