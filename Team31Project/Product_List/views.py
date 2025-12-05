from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product

def index(request):
    products = Product.objects.filter(active=True)
    return render(request, "Product_List/Product_List.html", {"products": products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "Product_List/product_detail.html", {"product": product})

def add_to_basket(request, pk):
    if request.method != "POST":
        return redirect("product_detail", pk=pk)

    product = get_object_or_404(Product, pk=pk)

    cart = request.session.get("cart", {})
    str_id = str(product.id)
    cart[str_id] = cart.get(str_id, 0) + 1
    request.session["cart"] = cart
    request.session.modified = True

    messages.success(request, f"Added {product.name} to basket.")
    return redirect("product_detail", pk=pk)
