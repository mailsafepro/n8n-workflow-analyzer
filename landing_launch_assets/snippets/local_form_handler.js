// Local demo form handler.
// This prevents network submission and shows a confirmation message.
// Replace this with Formspree/Tally/Netlify Forms before production.

document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('[data-audit-form]');
  const message = document.querySelector('[data-form-message]');

  if (!form || !message) return;

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    message.textContent = 'Demo form only. In production, this will send a pilot request. Please do not submit secrets or workflow JSON here.';
    message.setAttribute('role', 'status');
    form.reset();
  });
});
