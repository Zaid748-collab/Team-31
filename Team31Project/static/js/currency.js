// ─── Currency Configuration ───────────────────────────────────────────────
const CURRENCIES = {
  GBP: { symbol: "£", name: "British Pound",   flag: "🇬🇧", rate: 1.00 },
  USD: { symbol: "$", name: "US Dollar",        flag: "🇺🇸", rate: 1.27 },
  EUR: { symbol: "€", name: "Euro",             flag: "🇪🇺", rate: 1.17 },
  JPY: { symbol: "¥", name: "Japanese Yen",     flag: "🇯🇵", rate: 191.5 },
  CAD: { symbol: "$", name: "Canadian Dollar",  flag: "🇨🇦", rate: 1.73 },
  AUD: { symbol: "$", name: "Australian Dollar",flag: "🇦🇺", rate: 1.96 },
};

const DEFAULT_CURRENCY = "GBP";
const STORAGE_KEY = "team31_currency";

// ─── State ─────────────────────────────────────────────────────────────────
let currentCurrency = localStorage.getItem(STORAGE_KEY) || DEFAULT_CURRENCY;

// ─── Core Functions ─────────────────────────────────────────────────────────

/**
 * Convert a base (GBP) price to the currently selected currency.
 * @param {number} basePrice  Price in GBP
 * @returns {string}          Formatted price string e.g. "$12.99"
 */
function convertPrice(basePrice) {
  const currency = CURRENCIES[currentCurrency];
  const converted = basePrice * currency.rate;
  const formatted = converted >= 100
    ? converted.toFixed(0)
    : converted.toFixed(2);
  return `${currency.symbol}${formatted}`;
}

/**
 * Set a new active currency and refresh all prices on the page.
 * @param {string} code  Currency code e.g. "USD"
 */
function setCurrency(code) {
  if (!CURRENCIES[code]) return;
  currentCurrency = code;
  localStorage.setItem(STORAGE_KEY, code);
  refreshPrices();
  updateSwitcherUI();
  // Notify Django session (optional — keeps server in sync)
  fetch(`/set-currency/?code=${code}`, { method: "POST",
    headers: { "X-CSRFToken": getCookie("csrftoken") }
  }).catch(() => {}); // silent fail — localStorage is the source of truth
}

/**
 * Re-render every element that carries a data-base-price attribute.
 * Add  data-base-price="9.99"  to any element that displays a price.
 */
function refreshPrices() {
  document.querySelectorAll("[data-base-price]").forEach(el => {
    const base = parseFloat(el.dataset.basePrice);
    if (!isNaN(base)) el.textContent = convertPrice(base);
  });
}

/** Update the switcher button label to reflect the active currency. */
function updateSwitcherUI() {
  const currency = CURRENCIES[currentCurrency];
  const btn = document.getElementById("currency-btn");
  if (btn) {
    btn.innerHTML = `${currency.flag} ${currentCurrency} <span class="currency-chevron">▾</span>`;
  }
  // Highlight active option in dropdown
  document.querySelectorAll(".currency-option").forEach(opt => {
    opt.classList.toggle("active", opt.dataset.code === currentCurrency);
  });
}

// ─── Dropdown Toggle ─────────────────────────────────────────────────────────
function toggleDropdown() {
  const dropdown = document.getElementById("currency-dropdown");
  const isOpen = dropdown.classList.toggle("open");
  document.getElementById("currency-btn").setAttribute("aria-expanded", isOpen);
}

// Close if user clicks elsewhere
document.addEventListener("click", e => {
  if (!e.target.closest("#currency-switcher")) {
    const dropdown = document.getElementById("currency-dropdown");
    if (dropdown) {
      dropdown.classList.remove("open");
      document.getElementById("currency-btn")?.setAttribute("aria-expanded", false);
    }
  }
});

// ─── CSRF helper (Django) ────────────────────────────────────────────────────
function getCookie(name) {
  const match = document.cookie.match(new RegExp(`(^| )${name}=([^;]+)`));
  return match ? decodeURIComponent(match[2]) : "";
}

// ─── Initialise on DOM ready ─────────────────────────────────────────────────
document.addEventListener("DOMContentLoaded", () => {
  // Build dropdown options dynamically
  const list = document.getElementById("currency-list");
  if (list) {
    list.innerHTML = "";
    Object.entries(CURRENCIES).forEach(([code, info]) => {
      const li = document.createElement("li");
      li.className = "currency-option";
      li.dataset.code = code;
      li.innerHTML = `
        <span class="currency-flag">${info.flag}</span>
        <span class="currency-code">${code}</span>
        <span class="currency-name">${info.name}</span>
        <span class="currency-symbol">${info.symbol}</span>
      `;
      li.addEventListener("click", () => {
        setCurrency(code);
        toggleDropdown();
      });
      list.appendChild(li);
    });
  }

  updateSwitcherUI();
  refreshPrices();
});