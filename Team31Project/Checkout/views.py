from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from Checkout.models import Order, OrderItem
from Product_List.models import Product
from User_Basket.models import Cart, CartItem


@login_required
def checkout_view(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        items = CartItem.objects.filter(cart=cart) if cart else []
        display_items = [
            {
                "id": i.product.id,
                "name": i.product.name,
                "price": i.product.price,
                "image_url": i.product.image_url,
                "quantity": i.quantity,
            }
            for i in items
        ]
        total = sum(i["price"] * i["quantity"] for i in display_items)
    else:
        basket = request.session.get('basket', {})
        items = [{'product': Product.objects.get(id=pid), 'quantity': qty} for pid, qty in basket.items()]
        display_items = [
            {
                "id": i['product'].id,
                "name": i['product'].name,
                "price": i['product'].price,
                "image_url": i['product'].image_url,
                "quantity": i['quantity'],
            }
            for i in items
        ]
        total = sum(i["price"] * i["quantity"] for i in display_items)

    return render(request, 'Checkout/checkout.html', {
        'items': display_items,
        'total': total
    })


@login_required
def confirm_checkout(request):
    cart = Cart.objects.filter(user=request.user).first()
    items = CartItem.objects.filter(cart=cart) if cart else []

    if not items:
        return JsonResponse({"success": False, "message": "Basket is empty."})

    total = sum(i.product.price * i.quantity for i in items)

    order = Order.objects.create(
        user=request.user,
        total_price=total,
        status="Pending"
    )

    for item in items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )

    # Clear cart
    items.delete()

    return JsonResponse({"success": True, "message": "Your order has been processed!"})
