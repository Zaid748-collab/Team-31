from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Cart, CartItem
from Product_List.models import Product

@require_POST
def add_to_basket(request, product_id):
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
        item, created = CartItem.objects.get_or_create(
            cart=cart,
            product_id=product_id,
            defaults={'quantity': 1}
        )
        if not created:
            item.quantity += 1
            item.save()
        items = CartItem.objects.filter(cart=cart)
        total = sum(i.product.price * i.quantity for i in items)
    else:
        basket = request.session.get('basket', {})
        basket[str(product_id)] = basket.get(str(product_id), 0) + 1
        request.session['basket'] = basket
        items = [{'product': Product.objects.get(id=pid), 'quantity': qty} for pid, qty in basket.items()]
        total = sum(i['product'].price * i['quantity'] for i in items)

    basket_data = {
        "items": [
            {
                "id": i.product.id,
                "name": i.product.name,
                "price": i.product.price,
                "image_url": i.product.image_url,
                "quantity": i.quantity,
            } if hasattr(i, "product") else {
                "id": i['product'].id,
                "name": i['product'].name,
                "price": i['product'].price,
                "image_url": i['product'].image_url,
                "quantity": i['quantity'],
            }
            for i in items
        ],
        "total": total,
    }
    return JsonResponse(basket_data)


@require_POST
def remove_from_basket(request, product_id):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            item = CartItem.objects.filter(cart=cart, product_id=product_id).first()
            if item:
                if item.quantity > 1:
                    item.quantity -= 1
                    item.save()
                else:
                    item.delete()
        items = CartItem.objects.filter(cart=cart) if cart else []
        total = sum(i.product.price * i.quantity for i in items)
    else:
        basket = request.session.get('basket', {})
        if str(product_id) in basket:
            if basket[str(product_id)] > 1:
                basket[str(product_id)] -= 1
            else:
                basket.pop(str(product_id))
        request.session['basket'] = basket
        items = [{'product': Product.objects.get(id=pid), 'quantity': qty} for pid, qty in basket.items()]
        total = sum(i['product'].price * i['quantity'] for i in items)

    basket_data = {
        "items": [
            {
                "id": i.product.id,
                "name": i.product.name,
                "price": i.product.price,
                "image_url": i.product.image_url,
                "quantity": i.quantity,
            } if hasattr(i, "product") else {
                "id": i['product'].id,
                "name": i['product'].name,
                "price": i['product'].price,
                "image_url": i['product'].image_url,
                "quantity": i['quantity'],
            }
            for i in items
        ],
        "total": total,
    }
    return JsonResponse(basket_data)


def basket_view(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        items = CartItem.objects.filter(cart=cart) if cart else []
        total = sum(i.product.price * i.quantity for i in items)
    else:
        basket = request.session.get('basket', {})
        items = [{'product': Product.objects.get(id=pid), 'quantity': qty} for pid, qty in basket.items()]
        total = sum(i['product'].price * i['quantity'] for i in items)

    basket_data = {
        "items": [
            {
                "id": i.product.id,
                "name": i.product.name,
                "price": i.product.price,
                "image_url": i.product.image_url,
                "quantity": i.quantity,
            } if hasattr(i, "product") else {
                "id": i['product'].id,
                "name": i['product'].name,
                "price": i['product'].price,
                "image_url": i['product'].image_url,
                "quantity": i['quantity'],
            }
            for i in items
        ],
        "total": total,
    }
    return JsonResponse(basket_data)