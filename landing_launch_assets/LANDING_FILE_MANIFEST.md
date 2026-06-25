# Landing File Manifest

## Files to integrate into the landing project

### Content files

- `content/sample-report.md` — sample report copy and structure.
- `content/privacy-safety.md` — privacy/safety copy.
- `content/form-copy.md` — form fields, microcopy, and success messages.
- `content/seo-metadata.md` — SEO and Open Graph metadata.

### Email templates

- `emails/01_reply_after_form.md` — first reply after lead form.
- `emails/02_anonymization_instructions.md` — workflow anonymization guide.
- `emails/03_audit_delivery.md` — audit pack delivery email.
- `emails/04_feedback_request.md` — pilot feedback request.

### HTML snippets

- `snippets/form_snippet.html` — safe pilot request form markup.
- `snippets/local_form_handler.js` — local/demo form handler with no network submission.

### Static pages

- `static/sample-report.html` — standalone sample report page.
- `static/privacy.html` — standalone privacy/safety page.
- `static/thank-you.html` — standalone thank-you page.

### Launch operations

- `LAUNCH_CHECKLIST.md` — pre-launch QA checklist.
- `DEPLOY.md` — deployment instructions.
- `IDE_INTEGRATION_PROMPT.md` — prompt for IDE integration.

## Recommended local run command

If the landing is static HTML:

```bash
cd landing
python3 -m http.server 5173
```

If the landing is Vite/React:

```bash
cd landing
npm install
npm run dev
```

## Notes

- Do not upload workflow JSON through the landing form.
- Do not request credentials or secrets.
- Do not imply official n8n affiliation.
- Keep the form as pilot request only.
