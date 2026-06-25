# Batch 002 Public Mixed Corpus Evaluation

## 1. Batch Summary

- **Target workflows:** 50
- **Actual workflows:** 36 (14 lost to cross-category dedup + 2 failed downloads)
- **Categories:** ai (14), sales (8), marketing (8), it_ops (7), support (4), document_ops (4), other (3)
- **Endpoint used:** `https://api.n8n.io/templates/search`
- **Total failed downloads:** 2 (ai: 1, support: 1)
- **Suspicious key files:** 1 (`sessionKey` in ai template 8573 — values not printed)
- **Output directory:** `examples/corpus/batch_002_public_mixed`
- **Audit pack:** `examples/audit_packs/batch_002_public_mixed`

## 2. Download Summary By Category

| Category | Target | Downloaded | Failed | Skipped | Endpoint | Suspicious |
|----------|--------|------------|--------|---------|----------|------------|
| ai | 15 | 14 | 1 | 0 | /templates/search | 1 |
| sales | 8 | 8 | 0 | 0 | /templates/search | 0 |
| marketing | 8 | 8 | 0 | 0 | /templates/search | 0 |
| it_ops | 7 | 7 | 0 | 0 | /templates/search | 0 |
| support | 5 | 4 | 1 | 0 | /templates/search | 0 |
| document_ops | 4 | 4 | 0 | 0 | /templates/search | 0 |
| other | 3 | 3 | 0 | 0 | /templates/search | 0 |

**Notes:** `it-ops` returned 0 results; `it ops` (space) worked. `document-ops` returned 0; `document ops` worked. Cross-category dedup reduced unique total from 48 to 36.

## 3. Analyzer Summary

| Metric | Before (v0.7.1) | After (v0.8) |
|--------|-----------------|---------------|
| Workflow count | 36 | 36 |
| Total findings | 156 | 155 |
| Critical findings | 1 | 1 |
| High findings | 9 | 8 |
| Medium findings | 130 | 130 |
| Low findings | 16 | 16 |
| Overall risk score | 23/100 | 15/100 |
| Cost risk score | 61/100 | 41/100 |
| Operational risk score | 0/100 | 0/100 |
| Complexity score | 15/100 | 5/100 |
| Parser warnings | 131 | 79 |
| Unknown node types | 28 | 6 |
| Credential references | 241 | 241 |
| Trigger nodes | 59 | 59 |

**Top node categories (v0.8):** control_flow (544), transform (224), ai (138), http_api (96), trigger (48), spreadsheet (41)

## 4. Top Workflows

| Rank | Workflow | Priority | Overall | Top Drivers |
|------|----------|----------|---------|-------------|
| 1 | Workflow Patterns & Boilerplate for Scaling up | Highest priority | 100 | LOOP_HTTP, LARGE_WF |
| 2 | Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | Highest priority | 100 | LOOP_HTTP, AI_NODE, LARGE_WF |
| 3 | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | Highest priority | 100 | LOOP_HTTP, AI_NODE, NO_ERROR_HANDLING |
| 4 | AI-powered WhatsApp chatbot for text, voice, images, and PDF with RAG | Highest priority | 100 | AI_NODE |
| 5 | Autonomous B2B Supplier Price Negotiation Agent | Highest priority | 100 | AI_NODE |
| 6 | Personalized email outreach with LinkedIn & Crunchbase data and Gemini AI review | High priority | 95 | LOOP_HTTP, AI_NODE |
| 7 | Automated AI YouTube Shorts Factory for ASMR (Seedance) | High priority | 95 | AI_NODE |
| 8 | Automate video creation with Veo3 and auto-post to Instagram, TikTok via Blotato | High priority | 95 | AI_NODE |
| 9 | Track AI agent token usage and estimate costs in Google Sheets | High priority | 90 | AI_NODE |
| 10 | Nutrition tracker & meal logger with Telegram, Gemini AI and Google Sheets | High priority | 90 | AI_NODE, LARGE_WF |

## 5. Findings Breakdown

### By Rule ID

| Rule ID | Count | Description |
|---------|-------|-------------|
| AI_NODE | 83 | AI/LLM node detected |
| NO_ERROR_HANDLING | 36 | Missing error workflow |
| MANY_HTTP | 15 | Multiple HTTP Request nodes |
| LOOP_HTTP | 8 | Loop/batch combined with HTTP request |
| HIGH_FAN_OUT | 7 | Node with 5+ outgoing connections |
| LARGE_WF | 5 | Workflow with many nodes |
| WEBHOOK_CHAIN | 1 | Webhook chaining to internal URLs |

**Note:** FREQ_POLL no longer shows here. The old 1 finding was a false positive (0 `minutesInterval` defaulted to 0, triggering `val <= 0`). The v0.8 fix requires explicit `minutesInterval > 0` and `>= 5`. No schedule trigger in this corpus is truly frequent (all are ≥6 hours or default/hourly).

### By Severity

| Severity | Before | After |
|----------|--------|-------|
| critical | 1 | 1 |
| high | 9 | 8 |
| medium | 130 | 130 |
| low | 16 | 16 |

### By Category

| Category | Count |
|----------|-------|
| cost | 107 |
| reliability | 36 |
| complexity | 12 |
| operational | 1 |

## 6. Unknown / New Node Types (v0.8 — Classified)

**28 unknown types reduced to 6 remaining (all community):**

### Classified in v0.8 (22 types)

The following node types were classified in v0.8 via exact entries and keyword case-insensitivity fix:

| Node Type | Classification |
|-----------|----------------|
| `n8n-nodes-base.httpRequestTool` | `http_api` |
| `n8n-nodes-base.googleSheetsTool` | `spreadsheet` |
| `n8n-nodes-base.googleSheetsTrigger` | `trigger` |
| `n8n-nodes-base.googleDocs` | `document` |
| `n8n-nodes-base.cryptoTool` | `transform` |
| `n8n-nodes-base.dataTable` | `transform` |
| `n8n-nodes-base.dateTimeTool` | `transform` |
| `n8n-nodes-base.notion` | `crm` |
| `n8n-nodes-base.rssFeedReadTool` | `scraping` |
| `n8n-nodes-base.wooCommerceTool` | `crm` |
| `n8n-nodes-base.youTube` | `marketing` |
| `n8n-nodes-base.twilioTrigger` | `trigger` |
| `n8n-nodes-base.typeformTrigger` | `trigger` |
| `n8n-nodes-base.errorTrigger` | `trigger` |
| `n8n-nodes-base.evaluation` | `control_flow` |
| `n8n-nodes-base.evaluationTrigger` | `trigger` |
| `n8n-nodes-base.executeWorkflowTrigger` | `trigger` |
| `n8n-nodes-base.extractFromFile` | `document` |
| `n8n-nodes-base.googleAds` | `marketing` |
| `n8n-nodes-base.googleContactsTool` | `crm` |
| `n8n-nodes-base.googleTasksTool` | `crm` |
| `@elevenlabs/n8n-nodes-elevenlabs.elevenLabs` | `ai` |

### Remaining community types (6)

These are community packages that can be classified in future work:

| Node Type | Proposed Classification |
|-----------|------------------------|
| `@bedrijfsdatanl/n8n-nodes-prospectpro.prospectpro` | community / crm |
| `@bedrijfsdatanl/n8n-nodes-prospectpro.prospectproTrigger` | community / trigger |
| `n8n-nodes-browseract.browserAct` | community / scraping |
| `n8n-nodes-connectsafely-ai.connectSafelyLinkedIn` | community / marketing |
| `n8n-nodes-serpapi.serpApi` | community / scraping |
| `n8n-nodes-upload-post.uploadPost` | community / marketing |

**Parser warnings dropped from 131 → 79** (52 fewer, all community-type remaining).

## 7. Suspicious Keys / Safety

- **1 suspicious key found:** `sessionKey` in workflow 8573 (Monitor n8n community...)
- **Values not printed** in any report output — confirmed.
- **Recommendation:** The suspicious key scan works correctly. No change needed.

## 8. Report Quality Review (v0.8)

| Question | Assessment |
|----------|------------|
| Does executive_summary remain readable with 50 workflows? | YES — executive summary is category-driven, not workflow-by-workflow |
| Does client_action_plan become too long? | FIXED — truncation added for error handling list and unknown types list (>10 items get "... and N more") |
| Are recommendations too generic? | NO — recommendations reference specific workflow names |
| Does technical_report become too large? | FIXED — truncation added for Workflow Summaries (30 max), Workflow Inventory (30 max), Cost/Op/Complexity findings (20 each), Node Types (20), Unknown types (20), Workflow-Level Details (10). Remaining items show "... and N more (table truncated for readability)". |
| Does grouping still work? | YES — AI exposure grouped by workflow, error handling grouped |

## 9. Comparison vs Demo Corpus

| Metric | Demo Corpus (10) | Batch 002 Before (v0.7.1) | Batch 002 After (v0.8) | Delta (v0.7→v0.8) |
|--------|-----------------|--------------------------|------------------------|--------------------|
| Workflow count | 10 | 36 | 36 | — |
| Total findings | 31 | 156 | 155 | -1 |
| Findings per workflow | 3.1 | 4.3 | 4.3 | — |
| Critical findings | 0 | 1 | 1 | — |
| High findings | 3 | 9 | 8 | -1 |
| Medium findings | 19 | 130 | 130 | — |
| Low findings | 5 | 16 | 16 | — |
| Unknown node types | 0 | 28 | 6 | -22 |
| Parser warnings | 0 | 131 | 79 | -52 |
| Credential references | 58 | 241 | 241 | — |
| Dominant rule | AI_NODE (16) | AI_NODE (83) | AI_NODE (83) | — |
| LOOP_HTTP count | 3 | 8 | 8 | — |
| NO_ERROR_HANDLING count | 7 | 36 | 36 | — |

## 10. v0.8 Changes Applied

### Completed

| Change | Before | After | Status |
|--------|--------|-------|--------|
| Classify unknown node types | 28 unknown | 6 unknown (community-only) | Done |
| Fix FREQ_POLL false positives | FREQ_POLL found 1 (false positive) | FREQ_POLL finds 0 (correct — no truly frequent schedules) | Done |
| Keyword case-insensitivity fix | Mixed-case keywords didn't match | All keywords match case-insensitively | Done |
| Report truncation (30 workflows + 100 findings) | Full report for all 36 workflows | Truncated at 30 workflows, 20 findings per table, 10 details | Done |
| Client action plan truncation | All items listed | Items truncated at 10 per list with "... and N more" | Done |
| Parser warnings | 131 | 79 | Done |

### Remaining for v0.9+

1. **Community node classification** — 6 remaining community types (`@bedrijfsdatanl`, `n8n-nodes-browseract`, etc.) could be classified in a future pass.
2. **Operational risk detection** — Only 1 operational finding (WEBHOOK_CHAIN) across 36 workflows. The rules may need auditing for real operational patterns in public templates.
3. **Add manualTrigger detection/filter** — Many downloaded templates use `manualTrigger` which could benefit from a dedicated filter.
4. **AI node sub-categorization** — Distinguish between embedding models, chat models, and agent nodes for more granular cost modeling.

## 11. Decision

> **Ready for 100-workflow corpus.**

v0.8 addressed all P0 items from the v0.7.1 eval:

1. ✅ **Classified 28 missing node types** — 22 exact entries added + keyword case-insensitivity fix.
2. ✅ **Fixed FREQ_POLL** — No more false positives; correctly handles all scheduleTrigger parameter shapes.
3. ✅ **Reduced parser warnings** — 131 → 79 (remaining are community types only).
4. ✅ **Report scaling** — Truncation triggers automatically when >30 workflows or >100 findings.

Decision: **Ready for 100+ workflow corpus.**
