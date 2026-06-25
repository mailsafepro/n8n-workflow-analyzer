# Audit Pack Review Checklist

Use this checklist to review any audit pack before sharing with a client, pilot user, or stakeholder.

## Security

| # | Check | Pass/Fail | Notes |
|---|-------|-----------|-------|
| 1 | No credential values printed in any report file | ☐ | |
| 2 | No raw authorization headers or tokens visible | ☐ | |
| 3 | No customer PII (names, emails, IPs, addresses) | ☐ | |
| 4 | No internal URL patterns that reveal network topology | ☐ | |
| 5 | No API keys, secrets, or passwords in output | ☐ | |
| 6 | Credential reference count shown but values never exposed | ☐ | |
| 7 | "Secrets not inspected" caveat present in executive summary | ☐ | |

## Quality

| # | Check | Pass/Fail | Notes |
|---|-------|-----------|-------|
| 8 | Workflow names are readable and meaningful | ☐ | |
| 9 | Unknown/unclassified node types count is zero or documented | ☐ | |
| 10 | Top-ranked workflow is genuinely the most concerning | ☐ | |
| 11 | Recommendations reference specific workflows or nodes | ☐ | |
| 12 | Executive summary is understandable without domain expertise | ☐ | |
| 13 | Findings are grouped or deduplicated meaningfully | ☐ | |
| 14 | Risk scores have context (what does 40/100 mean?) | ☐ | |
| 15 | All section headers are present and correctly formatted | ☐ | |
| 16 | Version string matches the tool version | ☐ | |
| 17 | No "(s)" pluralization template artifacts | ☐ | |
| 18 | "No operational findings" does not contradict visible findings | ☐ | |

## Commercial

| # | Check | Pass/Fail | Notes |
|---|-------|-----------|-------|
| 19 | Report clearly articulates a pain point | ☐ | |
| 20 | Clear next action is recommended | ☐ | |
| 21 | Value is evident even on first skim | ☐ | |
| 22 | No overclaiming (e.g., "guaranteed savings") | ☐ | |
| 23 | Cost estimates are properly caveated as heuristic | ☐ | |
| 24 | Report does not claim to be an official n8n product | ☐ | |
| 25 | Report does not claim to be a security or compliance audit | ☐ | |

## Decision

| Outcome | Criteria | Check |
|---------|----------|-------|
| **Ready to share** | All security checks pass + at least 8/10 quality checks pass | ☐ |
| **Needs edits** | All security checks pass + 5–7 quality checks pass | ☐ |
| **Reject** | Any security check fails OR fewer than 5 quality checks pass | ☐ |

**Reviewer:** _________________ **Date:** _________________ **Decision:** _____________

## Quick checklist (for repeated use)

```
☐ No secrets printed          ☐ Workflow names readable
☐ No credential values        ☐ Recommendations specific
☐ Executive summary clear     ☐ Caveats present
☐ Top workflow makes sense    ☐ Version string correct
☐ No overclaiming             ☐ No template artifacts
```
