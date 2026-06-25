# Real Workflow Corpus Evaluation — v0.5

## 1. Corpus Summary

| Field | Value |
|-------|-------|
| Corpus path | `examples/real_workflows/` |
| JSON files | 10 |
| Workflows parsed | 10 |
| Invalid files | 0 |
| Empty files | 0 |
| Generated audit pack | `examples/audit_pack_real_workflows/` |
| Analyzer version | v0.5.0 |

## 2. Execution Result

| Field | Value |
|-------|-------|
| Command | `PYTHONPATH=src python -m n8n_cost_analyzer.cli analyze ./examples/real_workflows --audit-pack ./examples/audit_pack_real_workflows --cost-model ./cost_model.example.yaml` |
| Exit code | 0 |
| Stdout | Summary printed, report generated |
| Stderr | None |
| Files generated | `executive_summary.md`, `client_action_plan.md`, `technical_report.md`, `analysis.json` |

## 3. Security / Sensitivity Check

No change from v0.4 evaluation. Reports do not expose secrets.

## 4. Analysis Summary

| Metric | v0.4 (pre-fix) | v0.5 (after AI fix + classifier) |
|--------|----------------|----------------------------------|
| Workflows parsed | 10 | 10 |
| Total findings | 56 → 31 (after AI fix) | 31 |
| Critical findings | 0 | 0 |
| High findings | 1 | 1 |
| Medium findings | * | 29 |
| Low findings | * | 1 |
| Overall risk score | 20 → 12 | 12 |
| Cost risk score | 59 → 35 | 35 |
| Unknown node types | **39** | **4** |
| Parser warnings | **115** | **14** |
| "Unnamed Workflow" | **7** | **0** |

## 5. Node Inventory

| Metric | v0.4 | v0.5 |
|--------|------|------|
| Total unique node types | 48 | 48 |
| Unknown node types | 39 | 4 |
| Trigger node count | 13 | 13 |
| Disabled node count | 0 | 0 |
| Credential reference count | 58 | 58 |

### Node Categories (new in v0.5)

| Category | Count |
|----------|-------|
| control_flow | 38 |
| ai | 31 |
| transform | 15 |
| unknown | 15 |
| trigger | 13 |
| storage | 6 |
| email | 6 |
| spreadsheet | 6 |
| http_api | 6 |
| communication | 4 |
| crm | 3 |
| calendar | 2 |
| devops | 1 |

### Remaining Unknown Node Types (4)

All are community/custom nodes that cannot be classified without knowing their behavior:

| Node Type | Occurrences | Notes |
|-----------|-------------|-------|
| `@blotato/n8n-nodes-blotato.blotato` | 10 | Social media publishing community node |
| `CUSTOM.scrapeNinja` | 3 | Custom web scraping node |
| `@tavily/n8n-nodes-tavily.tavilyTool` | 1 | AI search tool community node |
| `n8n-nodes-mcp.mcpClientTool` | 1 | MCP protocol client |

## 6. Connection Inventory

No change from v0.4 evaluation.

## 7. Top Workflows To Review

| Rank | Workflow | Overall | Cost | Critical | High | Top Drivers |
|------|----------|---------|------|----------|------|-------------|
| 1 | 💥 Viral TikTok Video Machine... | 95 | 65 | 0 | 1 | LOOP_HTTP, AI_NODE, NO_ERROR_HANDLING, MANY_HTTP, HIGH_FAN_OUT |
| 2 | RAG Workflow For Company... | 75 | 60 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 3 | ai | 75 | 60 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 4 | email | 60 | 45 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 5 | trackseo | 60 | 45 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 6 | chathub | 45 | 45 | 0 | 0 | AI_NODE |
| 7 | ScrapeNinja: AI generated... | 30 | 30 | 0 | 0 | AI_NODE |
| 8 | salesforce | 15 | 0 | 0 | 0 | NO_ERROR_HANDLING |
| 9 | scrape | 15 | 0 | 0 | 0 | NO_ERROR_HANDLING |
| 10 | backupn8n | 0 | 0 | 0 | 0 | — |

## 8. Findings Breakdown

### By Rule ID

| Rule ID | v0.4 Count | v0.5 Count | Change |
|---------|-----------|------------|--------|
| AI_NODE | ~50 | 21 | -58% (false positives eliminated) |
| NO_ERROR_HANDLING | 7 | 7 | unchanged |
| LOOP_HTTP | 1 | 1 | unchanged |
| MANY_HTTP | 1 | 1 | unchanged |
| HIGH_FAN_OUT | 1 | 1 | unchanged |

The 21 AI_NODE findings are now genuine (actual AI/LLM nodes), down from ~50 where half were false positives on `gmailTrigger`, `wait`, `gmail`, `gmailTool`.

## 9. Recommendation Quality Review

Recommendations unchanged from v0.4. All 4 recommendations remain useful.

## 10. Parser / Rule Gaps Resolved

### Fixed in v0.5

1. **Node classification** — 39 → 4 unknown types. Added `NODE_CATEGORIES` dict with ~120 entries plus keyword-based fallback. No `"ai"` substring keyword to avoid false positives.
2. **Workflow name extraction** — 7 "Unnamed Workflow" → 0. Fallback to filename stem for canvas export format.
3. **Collection name disambiguation** — unnamed workflows in multi-workflow files get `filename_N` suffix.
4. **Meta name extraction** — `workflow.meta.name` / `workflow.meta.title` checked before filename fallback.

### Remaining Gaps

1. **4 community/custom node types** cannot be classified without looking at their package metadata. These are genuinely unknown.
2. **AI_NODE fires on some infrastructure LangChain nodes** (memoryBufferWindow, outputParser, documentDefaultDataLoader, textSplitter). These are technically AI-adjacent but don't directly generate API costs. Could be split into a separate category.
3. **FREQ_POLL rule not firing** for `scheduleTrigger` in some canvases (need to verify).
4. **Pinecone vector store** still lacks a dedicated cost rule.

## 11. Product Readiness Assessment

| Question | v0.4 Answer | v0.5 Answer | Notes |
|----------|-----------|-----------|-------|
| Good enough for internal audit? | ALMOST | **YES** | Unknown types dropped from 39 to 4, all names resolved |
| Good enough to show to friendly user? | ALMOST | **YES** | Clean output now |
| Good enough for paid audit? | NO | **ALMOST** | Community node classification and some rule refinement needed |

## 12. v0.6 Recommendations

### P0 — Must Fix Before Paid Use

1. **Classify community nodes where possible** — @tavily/tavilyTool → ai, @blotato/blotato → marketing, n8n-nodes-mcp → devops, CUSTOM → custom
2. **Add FREQ_POLL detection for scheduleTrigger** — verify the rule works with new classifier

### P1 — Important

1. **Refine AI_NODE to exclude infrastructure LangChain nodes** (memoryBufferWindow, outputParser, documentDefaultDataLoader, textSplitter) — these don't generate API costs
2. **Add Pinecone/vector store cost rule** — these are managed databases with storage costs
3. **Report wording for "unknown" category** — distinguish community nodes from truly unknown

### P2 — Nice-to-Have

1. **Better cost model defaults** for AI inference costs
2. **Add `active` status parsing from canvas export metadata** (some canvas exports embed it in `meta`)
3. **Add per-filename workflow inventory** in reports

## 13. Decision

**Ready for friendly-user pilot**

The v0.5 changes (node classifier + name extraction) have eliminated the two biggest quality issues:
- 39 → 4 unknown node types (90% reduction)
- 7 → 0 "Unnamed Workflow" entries
- 115 → 14 parser warnings (88% reduction)
- 0 AI false positives on standard n8n types
- All existing functionality preserved and improved

The tool is now suitable for internal audits and friendly-user pilots. Remaining items (community node classification, rule refinement) are polish before paid use.

## Appendix: v0.5 File Changes

| File | Change |
|------|--------|
| `src/n8n_cost_analyzer/node_classifier.py` | **NEW** — deterministic classifier with ~120 exact types + keyword fallback |
| `src/n8n_cost_analyzer/parser.py` | Updated name extraction (filename fallback, meta name), import new classifier |
| `src/n8n_cost_analyzer/models.py` | Added `node_category_counts` to `NodeInventory` |
| `src/n8n_cost_analyzer/scoring.py` | Updated `compute_node_inventory` to use new classifier and track categories |
| `src/n8n_cost_analyzer/json_report.py` | Added `node_category_counts` to JSON output, version → 0.5.0 |
| `src/n8n_cost_analyzer/report.py` | Added Node Categories table, section header wording, version → 0.5.0 |
| `tests/test_node_classifier.py` | **NEW** — 12 tests covering all categories and false positive regression |
| `tests/test_parser.py` | Added 4 name fallback tests, updated `classify_node_type` assertion |
| `tests/test_json_report.py` | Added `node_category_counts` assertion |
| `tests/test_report.py` | Added Node Categories section test |
| `tests/test_real_workflow_corpus.py` | **NEW** — 5 tests verifying corpus requirements |
