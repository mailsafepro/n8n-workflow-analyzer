# Subject: How to anonymize n8n workflow exports before sending

Hi {{name}},

Before sending workflow exports, please anonymize them carefully.

## What to remove or replace

Please remove or replace:

- API keys;
- passwords;
- Authorization headers;
- Bearer tokens;
- access tokens;
- refresh tokens;
- client secrets;
- customer emails;
- customer names;
- internal domains or hostnames;
- production webhook URLs;
- sensitive sample payloads.

Use placeholders such as:

```text
YOUR_API_KEY
YOUR_TOKEN
user@example.com
internal.example.com
https://webhook.example.com/path
```

## What not to send

Please do not send:

- n8n credentials exports;
- `.env` files;
- API keys;
- screenshots containing secrets;
- customer data;
- production tokens.

## What is okay to send

Anonymized workflow JSON exports are enough.

The analyzer only needs workflow structure: nodes, connections, trigger types, and configuration shape. It does not need credential values.

## Final checklist

Before sending, confirm:

- [ ] no API keys;
- [ ] no Authorization/Bearer headers;
- [ ] no passwords;
- [ ] no tokens;
- [ ] no customer emails or PII;
- [ ] no internal hostnames;
- [ ] no production webhook URLs;
- [ ] no credential exports.

Once ready, send the anonymized JSON files as an attachment or shared folder.

Best,
{{your_name}}
