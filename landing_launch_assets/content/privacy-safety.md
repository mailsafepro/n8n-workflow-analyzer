# Privacy & Safety

## Workflow data should not need to leave your machine

The analyzer is designed for local/offline workflow audit scenarios. The goal is to inspect exported workflow definitions without requiring access to your n8n instance, credentials, or production systems.

## What the analyzer does

- Reads anonymized n8n workflow JSON exports.
- Performs static analysis of workflow structure.
- Detects cost-risk, reliability-risk, and complexity patterns.
- Counts credential references without inspecting credential values.
- Produces an audit pack with executive summary, action plan, technical report, and JSON output.

## What the analyzer does not do

- It does not execute workflows.
- It does not call the n8n API.
- It does not require access to your n8n instance.
- It does not require credentials, tokens, passwords, or secrets.
- It does not inspect credential values.
- It does not provide a security or compliance audit.
- It is not an official n8n product or service.

## Before sharing workflow exports

Please anonymize workflow exports before sharing them for review. Remove or replace:

- API keys;
- Authorization or Bearer headers;
- passwords;
- access tokens;
- refresh tokens;
- client secrets;
- customer emails or names;
- internal hostnames;
- production webhook URLs;
- sensitive sample payloads.

Use placeholders like:

```text
YOUR_API_KEY
example.com
user@example.com
internal.example
```

## Form safety

Do not paste workflow JSON, credentials, secrets, customer data, or production tokens into the pilot request form. The form is only for requesting an audit conversation.
