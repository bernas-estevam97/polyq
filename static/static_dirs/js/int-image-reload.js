// Inline onclick handlers are blocked by the CSP, so the reload button is wired here.
document.getElementById("int-reload")?.addEventListener("click", () => window.location.reload());
