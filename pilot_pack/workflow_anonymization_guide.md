# Workflow Anonymization Guide

Before sharing n8n workflow exports for analysis, anonymize any sensitive information.

## What to Anonymize

| Item | How to Anonymize |
|------|-----------------|
| API keys, tokens, passwords | Replace with placeholder values (`YOUR_API_KEY`) |
| Internal URLs | Replace `https://internal.company.com` with `https://internal.example.com` |
| Email addresses | Use `user@example.com` |
| IP addresses | Replace with `10.0.0.1` (RFC 1918) |
| Database connection strings | Remove credential parameters, keep structure |
| OAuth client IDs/secrets | Replace with placeholder values |
| Personal names | Replace with generic names (`John Doe`) |

## Quick Steps

1. Open each `.json` workflow export in a text editor
2. Search for sensitive patterns:
   - `"url":` — check for internal URLs
   - `"apiKey"`, `"password"`, `"token"`, `"secret"` — credential fields
   - `"email"`, `"authentication"` — sensitive configuration
3. Replace sensitive values while keeping JSON structure intact
4. Verify the workflow still parses: `n8n-cost-analyzer workflow.json`

## What Is Safe to Share

- Node types and connections
- Trigger configurations (cron schedules, webhook paths)
- Workflow structure and metadata
- Parameter structure (not values)

## Verification

After anonymization, run a quick scan to confirm no obvious secrets remain:

```bash
grep -i -E '(api.?key|password|secret|token)' workflow.json
```

If results only show placeholder values (e.g., `YOUR_API_KEY`), you are ready to share.
