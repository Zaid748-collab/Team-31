from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.filter(active=True)
    return render(request, "Product_List/Product_List.html", {"products": products})
