from django.shortcuts import render

def orders_view(request):
    # Placeholder list until you fetch real orders from the DB
    orders = []  # Example: later connect to Order model
    return render(request, 'Previous_Orders/orders.html', {'orders': orders})
