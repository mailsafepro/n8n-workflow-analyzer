# Corpus Evaluation Report — Batch 003

## Overview

- **Batch 002** (baseline): 36 mixed workflows from n8n official templates
- **Batch 003** (this run): 107 public workflows across 7 categories + 15 searches
- **Goal**: Stress-test v0.8 with larger, more diverse corpus (3× batch size)

## Download Summary

| Metric | Value |
|---|---|
| Raw downloaded | 153 (7 categories × ~5 + 15 searches × ~5) |
| Failed downloads | 7 |
| Unique workflows | 107 |
| Duplicates skipped | 46 |
| Suspicious `sessionKey` files | 11 (all Telegram Bot — values redacted) |
| Failed categories | ai (1), support (1), document_ops (1) |
| Failed searches | slack (1), scraping (1), notion (1), rag (1) |
| Glitch (removed) | `categorie_ai__manifest.json` contained 24 workflows (list export) — excluded from combined; dedup already prevented cross-file duplicates |

## Analyzer Summary

| Metric | Batch 002 | Batch 003 | Δ/Δ% |
|---|---|---|---|
| Workflows | 36 | 107 | +71 (+197%) |
| Total findings | 155 | 392 | +237 (+153%) |
| Critical | 1 | 1 | 0 |
| High | 8 | 25 | +17 |
| Risk score | 15 | 13 | -2 |
| Cost risk | 41 | 36 | -5 |
| Complexity score | 5 | 2 | -3 |
| Findings/workflow | 4.3 | 3.7 | -0.6 |
| Unknown node types | 6 | 36 | +30 |
| Credential refs | 241 | 587 | +346 |
| Parser warnings | 79 | 202 | +123 |

## Findings by Rule

| Rule | Batch 002 | Batch 003 | Δ | Per-wf (002) | Per-wf (003) |
|---|---|---|---|---|---|
| AI_NODE | 83 | 213 | +130 | 2.31 | 1.99 |
| DB_IN_LOOP | 0 | 3 | +3 | 0.00 | 0.03 |
| HIGH_FAN_OUT | 7 | 12 | +5 | 0.19 | 0.11 |
| LARGE_WF | 5 | 6 | +1 | 0.14 | 0.06 |
| LOOP_HTTP | 8 | 22 | +14 | 0.22 | 0.21 |
| MANY_HTTP | 15 | 31 | +16 | 0.42 | 0.29 |
| NO_ERROR_HANDLING | 36 | 99 | +63 | 1.00 | 0.93 |
| WEBHOOK_CHAIN | 1 | 6 | +5 | 0.03 | 0.06 |

## Findings by Severity

| Severity | Batch 002 | Batch 003 |
|---|---|---|
| Critical | 1 | 1 |
| High | 8 | 25 |
| Medium | 130 | 329 |
| Low | 16 | 37 |

## Top Node Categories

| Category | Batch 002 | Batch 003 | Δ |
|---|---|---|---|
| control_flow | 544 | 1064 | +520 |
| transform | 224 | 402 | +178 |
| ai | 138 | 321 | +183 |
| http_api | 96 | 198 | +102 |
| trigger | 48 | 136 | +88 |
| spreadsheet | 41 | 108 | +67 |
| unknown | 15 | 82 | +67 |
| communication | 33 | 59 | +26 |
| email | 26 | 56 | +30 |
| marketing | 12 | 40 | +28 |
| crm | 12 | 39 | +27 |
| database | 7 | 35 | +28 |

## Scalability Assessment

- **Large corpus mode**: ACTIVE (107 workflows, 392 findings — threshold >30 wf or >100 findings)
- **Technical report**: Truncated (392 findings > 100 threshold → per-workflow details truncated)
- **Execution time**: Estimate only — analyzer processed 107 workflows without crash
- **Memory**: No issues encountered

The 107-workflow corpus exercises the scaling logic that truncates per-workflow detail output (>30 workflows) and finding details (>100 findings). Both truncation points are working as designed.

## Notable Observations

1. **AI_NODE dominates scaling**: 213/392 findings (54%) are AI_NODE — consistent with Batch 002 (54%)
2. **NO_ERROR_HANDLING scales identically**: 99/392 (25%) vs 36/155 (23%) in Batch 002
3. **36 unknown node types** (vs 6 in Batch 002) — reflects inclusion of community nodes from search-based downloads
4. **107 workflows reached 10 risk score** — Batch 002 scored 15 with 36 workflows (smaller sample)
5. **No FREQ_POLL findings** — consistent with frequency-based triggers being uncommon in public templates
6. **Parser warnings**: 202 (Batch 003) vs 79 (Batch 002) — scales with workflow count

## Conclusion

v0.8 handles the 3× larger corpus correctly:
- Large corpus truncation works without errors
- No crashes, memory issues, or analysis degradation
- Fine-grained comparison between batches is possible
- Unknown node types are a growth vector as corpus expands
- The classifier's 22-entry expansion (Batch 002 → Batch 003) absorbed some new types but 36 remain unknown

**Recommendation**: v0.8 is ready for production use at scale.
