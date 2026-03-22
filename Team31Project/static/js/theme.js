// ========== THEME MANAGER ==========
(function() {
    try {
        const savedTheme = localStorage.getItem("theme");
        if (savedTheme === "dark" || savedTheme === "light") {
            document.documentElement.setAttribute("data-theme", savedTheme);
        } else {
            document.documentElement.setAttribute("data-theme", "light");
        }
    } catch (e) {
        console.log("Theme initialization failed:", e);
    }
})();

// Theme toggle functionality (will be called after DOM loads)
document.addEventListener("DOMContentLoaded", function() {
    const toggleBtn = document.getElementById("themeToggle");
    if (toggleBtn) {
        function getTheme() {
            return document.documentElement.getAttribute("data-theme") || "light";
        }
        
        function setTheme(theme) {
            document.documentElement.setAttribute("data-theme", theme);
            localStorage.setItem("theme", theme);
            toggleBtn.textContent = theme === "dark" ? "☀️" : "🌙";
        }
        
        toggleBtn.textContent = getTheme() === "dark" ? "☀️" : "🌙";
        
        toggleBtn.addEventListener("click", function(e) {
            e.preventDefault();
            setTheme(getTheme() === "dark" ? "light" : "dark");
        });
    }
});