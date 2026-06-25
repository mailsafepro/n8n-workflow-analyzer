# Deployment Instructions

## Static HTML

Run locally:

```bash
cd landing
python3 -m http.server 5173
```

Open:

```text
http://localhost:5173
```

Deploy options:

- Netlify drag-and-drop: upload the `landing/` folder.
- Cloudflare Pages: connect repository or upload static assets.
- Vercel static: deploy the `landing/` folder.

## Vite

Run locally:

```bash
cd landing
npm install
npm run dev
```

Build:

```bash
npm run build
```

Deploy the `dist/` folder to Vercel, Netlify, or Cloudflare Pages.

## Next.js

Run locally:

```bash
cd landing
npm install
npm run dev
```

Build:

```bash
npm run build
```

Deploy to Vercel.

## Form endpoint setup

Recommended simple options:

### Tally

- Create a Tally form.
- Link CTA buttons to the hosted form or embed it.
- Keep safety copy near the form.

### Formspree

- Create a Formspree endpoint.
- Replace `FORM_ENDPOINT` in the form action.
- Use POST method.
- Test one request before publishing.

### Netlify Forms

- Add `netlify` attribute to the form.
- Deploy on Netlify.
- Test from deployed site.

### mailto fallback

Use only if no form provider is configured.

## Metadata setup

Before deploy:

- replace canonical placeholder;
- update Open Graph URL if used;
- add favicon;
- test title and description.

## Pre-deploy smoke test

- [ ] Open homepage.
- [ ] Click main CTA.
- [ ] Submit test form.
- [ ] Open sample report.
- [ ] Open privacy/safety page.
- [ ] Test mobile viewport.
- [ ] Verify no secrets or private workflow data are embedded.
