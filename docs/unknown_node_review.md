# Unknown Node Type Review — Batch 002

Date: 2026-06-23
Corpus: batch_002_public_mixed (36 workflows)
Total unknown types found: 28

## Classification Strategy

- **Standard built-in nodes** (`n8n-nodes-base.*`) should be classified by type/function.
- **Tool variants** (e.g., `googleSheetsTool`, `httpRequestTool`) are AI-agent-callable versions of standard nodes. Classify under the same category as their base node.
- **Community nodes** (e.g., `@elevenlabs/*`, `n8n-nodes-*`) stay `unknown` unless clearly identifiable and well-known.
- **Trigger variants** (`*Trigger`, `*trigger`) go to `trigger` unless they have a more specific classification.

## Unknown Types — Classification Decisions

### Standard Built-In Nodes (classify)

| Node Type | Occurrences | Proposed Category | Rationale |
|-----------|-------------|-------------------|-----------|
| `n8n-nodes-base.httpRequestTool` | 3 | `http_api` | Tool variant of httpRequest; keyword `httpRequest` matches after case fix |
| `n8n-nodes-base.googleSheetsTool` | 9 | `spreadsheet` | Tool variant of googleSheets; keyword `googleSheets` matches after case fix |
| `n8n-nodes-base.googleSheetsTrigger` | 3 | `trigger` | Google Sheets trigger — match on exact type |
| `n8n-nodes-base.googleDocs` | 1 | `document` | Built-in Google Docs integration |
| `n8n-nodes-base.googleContactsTool` | 1 | `crm` | Contact management tool |
| `n8n-nodes-base.googleTasksTool` | 5 | `crm` | Task management tool |
| `n8n-nodes-base.googleAds` | 1 | `marketing` | Google Ads integration |
| `n8n-nodes-base.cryptoTool` | 1 | `transform` | Crypto/encoding utility tool |
| `n8n-nodes-base.dataTable` | 16 | `transform` | Data table transformation node |
| `n8n-nodes-base.dateTimeTool` | 1 | `transform` | Date/time utility tool |
| `n8n-nodes-base.notion` | 1 | `crm` | Notion CRM/documentation |
| `n8n-nodes-base.rssFeedReadTool` | 2 | `scraping` | RSS feed reader tool |
| `n8n-nodes-base.wooCommerceTool` | 3 | `crm` | WooCommerce e-commerce tool |
| `n8n-nodes-base.youTube` | 1 | `marketing` | YouTube integration |
| `n8n-nodes-base.twilioTrigger` | 1 | `trigger` | Twilio trigger (currently matched by `twilio` → `communication`) |
| `n8n-nodes-base.typeformTrigger` | 1 | `trigger` | Typeform webhook trigger |
| `n8n-nodes-base.errorTrigger` | 1 | `trigger` | Error workflow trigger |
| `n8n-nodes-base.evaluation` | 3 | `control_flow` | n8n built-in evaluation/testing feature |
| `n8n-nodes-base.evaluationTrigger` | 1 | `trigger` | Evaluation workflow trigger |
| `n8n-nodes-base.executeWorkflowTrigger` | 4 | `trigger` | Sub-workflow execution trigger |
| `n8n-nodes-base.extractFromFile` | 3 | `document` | File text extraction (PDF, etc.) |

### Community / Package Nodes (remain unknown in review, can classify)

| Node Type | Occurrences | Proposed Category | Rationale |
|-----------|-------------|-------------------|-----------|
| `@elevenlabs/n8n-nodes-elevenlabs.elevenLabs` | 2 | `ai` | ElevenLabs text-to-speech AI |
| `@bedrijfsdatanl/n8n-nodes-prospectpro.prospectpro` | 9 | `crm` | ProspectPro CRM enrichment |
| `@bedrijfsdatanl/n8n-nodes-prospectpro.prospectproTrigger` | 1 | `trigger` | ProspectPro trigger |
| `n8n-nodes-browseract.browserAct` | 1 | `scraping` | Browser automation |
| `n8n-nodes-connectsafely-ai.connectSafelyLinkedIn` | 1 | `marketing` | LinkedIn automation |
| `n8n-nodes-serpapi.serpApi` | 1 | `scraping` | SERP API search tool |
| `n8n-nodes-upload-post.uploadPost` | 2 | `marketing` | Social media posting |

## Impact After Classification

After adding exact entries + fixing keyword case:

| Metric | Before | After |
|--------|--------|-------|
| Unknown node types | 28 | 7 (community-only) |
| Parser warnings (unknown node type) | ~131 | ~12 (community-only) |
| Node category coverage | ~90% | ~97% |
