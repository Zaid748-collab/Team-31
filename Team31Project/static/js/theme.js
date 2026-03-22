// ─── Theme Configuration ─────────────────────────────────────────────────────
const THEME_KEY = "team31_theme";

// Apply theme immediately before page renders (prevents flash)
(function () {
    const saved = localStorage.getItem(THEME_KEY) || "light";
    document.documentElement.setAttribute("data-theme", saved);
})();

// ─── Toggle & Update ─────────────────────────────────────────────────────────
function updateToggleIcon() {
    const btn = document.getElementById("themeToggle");
    if (btn) {
        btn.textContent = document.documentElement.getAttribute("data-theme") === "dark" ? "☀️" : "🌙";
    }
}

function toggleTheme() {
    const current = document.documentElement.getAttribute("data-theme") || "light";
    const next = current === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    localStorage.setItem(THEME_KEY, next);
    updateToggleIcon();
}

// ─── Initialise on DOM ready ──────────────────────────────────────────────────
document.addEventListener("DOMContentLoaded", function () {
    updateToggleIcon();
    const btn = document.getElementById("themeToggle");
    if (btn) {
        btn.addEventListener("click", function (e) {
            e.preventDefault();
            toggleTheme();
        });
    }
});