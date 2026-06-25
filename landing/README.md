# n8n Workflow Cost & Risk Analyzer Landing

Landing page for the n8n Workflow Cost & Risk Analyzer — a local/offline tool that audits n8n workflow exports for cost risks, reliability gaps, credential governance issues, and operational complexity.

## Run locally

```bash
cd landing
python3 -m http.server 5173
```

Then open **http://localhost:5173** in your browser.

## Structure

```
landing/
├── index.html              # Main landing page
├── sample-report.html      # Standalone sample report page
├── privacy.html            # Privacy & safety page
├── thank-you.html          # Post-submit confirmation page
├── emails/                 # Email templates for audit workflow
│   ├── 01_reply_after_form.md
│   ├── 02_anonymization_instructions.md
│   ├── 03_audit_delivery.md
│   └── 04_feedback_request.md
├── LAUNCH_CHECKLIST.md     # Pre-launch checklist
├── DEPLOY.md               # Deployment instructions
└── README.md
```

## What this is

- Static HTML landing page (no build step required)
- Tailwind CSS via CDN
- Icons via Iconify CDN
- Google Fonts (Inter + Oswald)
- No bundler, no npm, no build step

## Pages

| Path | Description |
|------|-------------|
| `/` | Main homepage with hero, report preview, scope, privacy, pricing, form |
| `/sample-report.html` | Sample audit output showing metrics, risk patterns, and recommendations |
| `/privacy.html` | Privacy & safety info — local/offline analysis, anonymization guidance |
| `/thank-you.html` | Confirmation shown after form submission |

## Form behavior

- **Demo mode** (current): form intercepts submit via JS, shows confirmation. No network request.
- **Production**: replace form handler with Formspree, Tally, Netlify Forms, or a custom endpoint.

Do not ask users to paste workflow JSON, credentials, secrets, customer data, or production tokens through the landing form.

## Deploy to Fly.io

### Prerequisites

- [flyctl](https://fly.io/docs/flyctl/install/) installed and logged in (`fly auth login`)
- Docker installed (or use Fly's remote builder)

### One-time setup

```bash
cd landing
fly launch --generate-name --region mad --no-deploy
```

This creates the app on Fly.io without deploying yet.

### Deploy

```bash
cd landing
fly deploy
```

### Visit

```bash
fly open
```

Or open the URL shown in the deploy output (e.g. `https://n8n-analyzer-landing.fly.dev`).

### Verify

```bash
curl -sI https://n8n-analyzer-landing.fly.dev/ | head -5
curl -sI https://n8n-analyzer-landing.fly.dev/sample-report.html | head -3
curl -sI https://n8n-analyzer-landing.fly.dev/privacy.html | head -3
```

All should return `HTTP/2 200`.

### Notes

- Fly.io manages HTTPS automatically.
- No custom domain required — the `.fly.dev` URL is production-ready.
- The Dockerfile uses `nginx:alpine` (~7 MB image). No build step needed.
- To update: edit files, then `fly deploy` again.
- To destroy: `fly apps destroy n8n-analyzer-landing`.

## Notes

- Not affiliated with n8n GmbH.
- No analytics, tracking, or external API calls in demo mode.
