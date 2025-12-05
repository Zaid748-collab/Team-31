from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from User_Basket.models import Cart, CartItem
from Product_List.models import Product
from Previous_Orders.models import Order, OrderItem

def checkout_view(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        items = CartItem.objects.filter(cart=cart) if cart else []
        total = sum(i.product.price * i.quantity for i in items)
    else:
        basket = request.session.get('basket', {})
        items = [{'product': Product.objects.get(id=pid), 'quantity': qty} for pid, qty in basket.items()]
        total = sum(i['product'].price * i['quantity'] for i in items)

    return render(request, "checkout.html", {"items": items, "total": total})

@require_POST
def confirm_checkout(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            order = Order.objects.create(user=request.user, total=sum(i.product.price * i.quantity for i in cart.items.all()))
            for item in cart.items.all():
                OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
            cart.items.all().delete()  # clear basket
    else:
        # handle guest checkout if needed
        pass
    return redirect("orders")  # show previous orders page