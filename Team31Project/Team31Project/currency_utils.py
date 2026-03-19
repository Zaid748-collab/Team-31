

from django.http import JsonResponse
from django.views.decorators.http import require_POST

# ─── Supported currencies (keep in sync with currency.js) ────────────────────

CURRENCIES = {
    "GBP": {"symbol": "£", "name": "British Pound",    "rate": 1.00},
    "USD": {"symbol": "$", "name": "US Dollar",         "rate": 1.27},
    "EUR": {"symbol": "€", "name": "Euro",              "rate": 1.17},
    "JPY": {"symbol": "¥", "name": "Japanese Yen",      "rate": 191.5},
    "CAD": {"symbol": "$", "name": "Canadian Dollar",   "rate": 1.73},
    "AUD": {"symbol": "$", "name": "Australian Dollar", "rate": 1.96},
}

DEFAULT_CURRENCY = "GBP"


# ─── View: POST /set-currency/?code=USD ──────────────────────────────────────

@require_POST
def set_currency_view(request):
    """Store the chosen currency in the user's session."""
    code = request.GET.get("code", DEFAULT_CURRENCY).upper()
    if code not in CURRENCIES:
        return JsonResponse({"error": "Unsupported currency"}, status=400)
    request.session["currency"] = code
    return JsonResponse({"status": "ok", "currency": code})


# ─── Context Processor ────────────────────────────────────────────────────────

def currency_context(request):
    """
    Makes {{ currency }}, {{ currency_symbol }}, and {{ currency_code }}
    available in every template automatically.

    Add to TEMPLATES[0]['OPTIONS']['context_processors'] in settings.py:
        'Team31Project.currency_utils.currency_context',
    """
    code = request.session.get("currency", DEFAULT_CURRENCY)
    if code not in CURRENCIES:
        code = DEFAULT_CURRENCY
    currency = CURRENCIES[code]
    return {
        "currency_code":   code,
        "currency_symbol": currency["symbol"],
        "currency_rate":   currency["rate"],
        "currency_name":   currency["name"],
    }


# ─── Helper: convert a GBP price in Python (e.g. for Checkout views) ─────────

def convert_price(base_gbp: float, currency_code: str) -> float:
    
    currency = CURRENCIES.get(currency_code, CURRENCIES[DEFAULT_CURRENCY])
    converted = base_gbp * currency["rate"]
    return round(converted, 2 if converted < 100 else 0)