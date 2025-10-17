from django.shortcuts import render

def index(request):
    return render(request, 'Previous_Orders/Previous_Orders.html', {'app_name': 'Previous_Orders'})