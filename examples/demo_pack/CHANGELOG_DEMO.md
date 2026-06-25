# Changelog — Demo Pack

## 0.7.1 (2026-06-23)

### Report Consistency Polish
- **Version unification**: All version strings now sourced from `version.py` (report, audit pack, JSON)
- **Priority labels**: Top Workflows table uses "Review Priority" columns; workflow summaries use "Priority" labels (Highest / High / Review recommended / Moderate / Low) instead of severity-based "Risk Level"
- **Operational / reliability**: Executive summary label changed to "Operational / reliability risk"; score context when reliability findings are present
- **Compact AI exposure**: Client action plan AI/API sublist shows top-5 workflows with AI node counts
- **Compact error handling**: Error-handling bullets list affected workflows as a compact sublist
- **Key findings**: Rewritten to avoid "immediately" language; separated high-severity cost patterns from AI/API exposure; AI exposure shown as sub-bullets
- **Executive summary counters**: Individual severity-count labels (e.g., "0 critical findings, 1 high finding")
- **164 tests** (up from 159 in v0.6, 177 in v0.7)

## 0.7.0 (2026-06-22)

### Demo Report Polish
- Created `pluralize()` helper for consistent singular/plural grammar
- Added `N/A` replacement for "Active: None" in workflow summaries
- Added risk score context table with "How to Interpret Risk Scores" guide
- Added "How to Read This Report" introduction section
- Added Workflow Summaries section with per-workflow narrative descriptions
- Grouped AI exposure findings by workflow with node counts
- Fixed Priority 0 report tone (critical→high)
- Added specific quick wins examples
- **177 tests**

## 0.6.0 (2026-06-21)

### Pre-Pilot Polish
- Classified all 4 unknown node types from the 10-workflow corpus
- Separated AI cost nodes into a dedicated category for more accurate cost scoring
- Verified FREQ_POLL with 4 new tests
- Improved report wording (community nodes section, severity labels)
- Created pilot pack structure
- **168 tests**, 0 unknown nodes, 0 parser warnings
