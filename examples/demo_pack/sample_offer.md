# Sample Offer — Self-Hosted Automation Cost Audit

## One-line offer

> Send me your anonymized n8n workflow exports and I'll return a cost/risk audit showing which automations may create runaway executions, AI/API cost exposure, or operational fragility.

## Who it is for

- **n8n self-hosted users** — running automation in production, paying for cloud infra
- **Automation consultants** — need a structured way to assess client workflows
- **SMBs with workflows in production** — running on manual trigger patterns without cost visibility
- **Teams worried about execution limits/costs** — approaching n8n cloud plan limits, or seeing unexpected API bills

## What you get

| Deliverable | Format | Content |
|-------------|--------|---------|
| Executive Summary | Markdown | Risk scores, top findings, business impact labels |
| Technical Report | Markdown | Full per-workflow analysis with node inventory |
| Client Action Plan | Markdown | Prioritized 7-day remediation plan with open questions |
| Analysis Data | JSON | Structured findings for custom processing or dashboards |

Each audit covers:

- **Cost risk** — AI/LLM nodes, frequent polling, loops with HTTP, many external API calls
- **Operational risk** — missing error handling, webhook chaining, DB in loops
- **Complexity risk** — large workflows, high fan-out, isolated nodes
- **Node inventory** — type classification, trigger count, credential references
- **Connection analysis** — edges, isolated nodes, fan-out patterns

## What it costs

*Pricing hypotheses — not validated. These are initial estimates for discussion.*

| Tier | Scope | Price | Use case |
|------|-------|-------|----------|
| **Pilot** | Up to 5 workflows, basic report | **Free** | Friendly-user feedback |
| **Lightweight** | Up to 10 workflows, standard audit | **€99–€199** | Quick health check |
| **Standard** | Up to 25 workflows, full audit + action plan | **€300–€500** | Team/org assessment |
| **Deep** | 25+ workflows, custom rules, delivery call | **€500–€900** | Enterprise or complex setup |

**What affects pricing:**
- Number of workflows (primary driver)
- Unknown/custom node types requiring manual classification
- Custom rule configuration or thresholds
- Delivery format (async document vs. live presentation)

## What I need from you

1. **Export your n8n workflows as JSON** — standard n8n export format
2. **Anonymize sensitive data** — remove or replace:
   - API keys, passwords, tokens with placeholders (`YOUR_API_KEY`)
   - Internal URLs (`internal.company.com` → `internal.example.com`)
   - Email addresses (`user@company.com` → `user@example.com`)
   - Personal names
3. **Send 3–10 representative workflows** — focus on production-critical ones
4. **(Optional) Share context** — which workflows are most concerning, what costs you're seeing

I do NOT need:
- Access to your n8n instance
- Credentials or secrets
- Customer or PII data
- Runtime logs or execution history (nice to have, not required)

## Delivery time

| Tier | Turnaround |
|------|------------|
| Pilot | 24–48 hours |
| Lightweight | 24–72 hours |
| Standard | 3–5 business days |
| Deep | 5–10 business days |

## Risks / caveats

- **Heuristic analysis** — based on node types and patterns, not actual execution data
- **Cost estimates are approximate** — based on configurable assumptions, not your actual API bills
- **Not official n8n** — independent tool, not affiliated with n8n GmbH
- **Not a security or compliance audit** — does not inspect credentials, data handling, or access controls
- **No runtime data** — unless you provide execution logs, the analysis is static only
- **Workflow context matters** — a "risky" pattern may be perfectly safe given the right input volumes; this is a screening, not a final verdict
