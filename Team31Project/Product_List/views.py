from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import Product, WishlistItem


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


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    WishlistItem.objects.get_or_create(
        user=request.user,
        product=product
    )

    # Option A: go directly to wishlist page
    return redirect("wishlist")


@login_required
def wishlist(request):
    items = WishlistItem.objects.filter(user=request.user).select_related("product")
    return render(request, "Product_List/wishlist.html", {"items": items})


@login_required
def remove_from_wishlist(request, item_id):
    WishlistItem.objects.filter(id=item_id, user=request.user).delete()
    return redirect("wishlist")