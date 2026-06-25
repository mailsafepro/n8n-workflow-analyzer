# Prompt for IDE AI — Integrate Landing Launch Assets

Actúa como Senior Frontend Engineer pragmático.

Contexto:
Ya existe una landing funcional en `landing/` para `n8n Workflow Cost & Risk Analyzer`.
Ahora se han creado assets de lanzamiento en `landing_launch_assets/`.

Objetivo:
Integrar los assets necesarios en la landing existente sin romper diseño ni funcionalidad.

NO tocar:
- `src/n8n_cost_analyzer/`
- tests del analyzer
- scripts del downloader
- core Python

SÍ hacer:
- añadir sample report page/section;
- añadir privacy/safety page/section;
- integrar copy de formulario seguro;
- asegurar que el formulario no hace POST externo salvo endpoint real configurado;
- añadir metadata SEO;
- añadir emails/checklist/deploy docs donde corresponda;
- validar localhost.

Archivos fuente:
- `landing_launch_assets/content/sample-report.md`
- `landing_launch_assets/content/privacy-safety.md`
- `landing_launch_assets/content/form-copy.md`
- `landing_launch_assets/content/seo-metadata.md`
- `landing_launch_assets/snippets/form_snippet.html`
- `landing_launch_assets/snippets/local_form_handler.js`
- `landing_launch_assets/static/sample-report.html`
- `landing_launch_assets/static/privacy.html`
- `landing_launch_assets/static/thank-you.html`
- `landing_launch_assets/emails/*.md`
- `landing_launch_assets/LAUNCH_CHECKLIST.md`
- `landing_launch_assets/DEPLOY.md`

Tareas:

1. Detectar stack de `landing/`:
   - HTML estático;
   - Vite/React;
   - Next;
   - otro.

2. Integrar sample report:
   - Si HTML estático: copiar/adaptar `static/sample-report.html` a `landing/sample-report.html`.
   - Si React/Vite: crear route/page/component equivalente o sección enlazada.

3. Integrar privacy/safety:
   - Si HTML estático: copiar/adaptar `static/privacy.html` a `landing/privacy.html`.
   - Si React/Vite: crear route/page/component equivalente o sección enlazada.

4. Integrar formulario:
   - Usar campos de `content/form-copy.md`.
   - No pedir workflow JSON ni secrets.
   - Si no hay endpoint real, interceptar submit y mostrar mensaje local.
   - Añadir nota: “Do not paste credentials, secrets, workflow JSON, customer data, or production tokens into this form.”

5. Añadir/actualizar metadata:
   - title;
   - meta description;
   - Open Graph;
   - canonical placeholder.

6. Copiar emails y docs:
   - Crear `landing/emails/` con los 4 emails.
   - Copiar `LAUNCH_CHECKLIST.md` y `DEPLOY.md` a `landing/` o raíz según convenga.
   - Crear/actualizar `landing/README.md` con instrucciones.

7. Validar:
   - landing arranca en localhost;
   - sample report link funciona;
   - privacy link funciona;
   - form no envía network request en modo demo;
   - no console errors evidentes;
   - responsive básico.

Reporte final:
- stack detectado;
- archivos modificados;
- archivos creados;
- comando para correr localhost;
- URL esperada;
- validaciones realizadas;
- pendientes antes de deploy.
