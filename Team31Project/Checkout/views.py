from django.shortcuts import render

def index(request):
    return render(request, 'Checkout/Checkout.html', {'app_name': 'Checkout'})