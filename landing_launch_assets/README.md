# Landing Launch Assets — n8n Workflow Cost & Risk Analyzer

This folder contains launch-ready copy, pages, snippets, email templates, checklists, and an IDE integration prompt for the landing page of **n8n Workflow Cost & Risk Analyzer**.

These assets are designed to be integrated into the existing `landing/` project without touching the Python analyzer core.

## What is included

```text
landing_launch_assets/
├── content/
│   ├── sample-report.md
│   ├── privacy-safety.md
│   ├── form-copy.md
│   └── seo-metadata.md
├── emails/
│   ├── 01_reply_after_form.md
│   ├── 02_anonymization_instructions.md
│   ├── 03_audit_delivery.md
│   └── 04_feedback_request.md
├── snippets/
│   ├── form_snippet.html
│   └── local_form_handler.js
├── static/
│   ├── sample-report.html
│   ├── privacy.html
│   └── thank-you.html
├── LAUNCH_CHECKLIST.md
├── DEPLOY.md
├── LANDING_FILE_MANIFEST.md
└── IDE_INTEGRATION_PROMPT.md
```

## Integration principle

Do **not** rebuild the landing from scratch. Use these assets to add:

- sample report page/section;
- privacy/safety page/section;
- safe pilot request form copy;
- launch checklist;
- deployment instructions;
- email templates;
- metadata/SEO.

## Safety principle

Do not ask users to upload workflows, credentials, secrets, tokens, customer data, or production URLs through the landing form. The form is for pilot requests only. Workflow files should only be shared later after anonymization instructions are sent.
