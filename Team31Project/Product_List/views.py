from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Product

def index(request):
   
    products = Product.objects.filter(active=True)

    category_type = request.GET.get("type")
    if category_type:
        products = products.filter(type__iexact=category_type)

    return render(request, "Product_List/Product_List.html", {
        "products": products,
        "selected_type": category_type,
    })


def product_detail(request, pk):
   
    product = get_object_or_404(Product, pk=pk)
    return render(request, "Product_List/product_detail.html", {
        "product": product,
    })


def add_to_basket(request, pk):
   
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request"}, status=400)

    product = get_object_or_404(Product, pk=pk)

    cart = request.session.get("cart", {})
    str_id = str(product.id)
    cart[str_id] = cart.get(str_id, 0) + 1
    request.session["cart"] = cart
    request.session.modified = True

    basket_items = []
    total = 0
    for pid, qty in cart.items():
        p = Product.objects.get(pk=pid)
        basket_items.append({
            "id": p.id,
            "name": p.name,
            "price": str(p.price),
            "image_url": p.image_url,
            "quantity": qty,
        })
        total += p.price * qty

    return JsonResponse({
        "items": basket_items,
        "total": str(total),
        "message": f"Added {product.name} to basket."
    })
