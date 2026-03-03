from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Avg, Count
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import Product, WishlistItem, Review


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

    # Reviews + rating stats
    reviews = Review.objects.filter(product=product).select_related("user")
    stats = reviews.aggregate(avg=Avg("rating"), count=Count("id"))

    user_review = None
    if request.user.is_authenticated:
        user_review = Review.objects.filter(product=product, user=request.user).first()

    return render(request, "Product_List/product_detail.html", {
        "product": product,
        "reviews": reviews,
        "avg_rating": stats["avg"] or 0,
        "review_count": stats["count"] or 0,
        "user_review": user_review,
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


# -------------------- WISHLIST --------------------

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


# -------------------- REVIEWS + RATINGS --------------------

@login_required
def submit_review(request, product_id):
    if request.method != "POST":
        return redirect("product_detail", pk=product_id)

    product = get_object_or_404(Product, pk=product_id)

    rating = request.POST.get("rating")
    comment = (request.POST.get("comment") or "").strip()

    # validate rating 1..5
    try:
        rating_int = int(rating)
        if rating_int < 1 or rating_int > 5:
            raise ValueError
    except Exception:
        messages.error(request, "Rating must be a number between 1 and 5.")
        return redirect("product_detail", pk=product.id)

    # 1 review per user per product (update if exists)
    Review.objects.update_or_create(
        user=request.user,
        product=product,
        defaults={"rating": rating_int, "comment": comment},
    )

    messages.success(request, "Your review was saved ✅")
    return redirect("product_detail", pk=product.id)