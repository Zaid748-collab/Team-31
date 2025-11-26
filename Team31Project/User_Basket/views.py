from django.shortcuts import render

def basket_view(request):
    # For now, we’ll show placeholder content until DB integration
    basket_items = []  # Example: later replace with real data
    basket_total = 0
    return render(request, 'User_Basket/basket.html', {
        'basket_items': basket_items,
        'basket_total': basket_total
    })
