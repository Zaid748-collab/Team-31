from django.shortcuts import render

def orders_view(request):
    orders = []  
    return render(request, 'Previous_Orders/orders.html', {'orders': orders})
