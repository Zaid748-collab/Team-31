from django.shortcuts import render
from .models import Product

def index(request):
    return render(request, 'Product_List/Product_List.html', {'app_name': 'Product_List'})

def index(request):
    products = Product.objects.filter(active=True)
    return render(request, 'Product_List/Product_List.html', {'products': products})