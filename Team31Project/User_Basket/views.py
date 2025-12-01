from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from Product_List.models import Product


def index(request):
    return render(request, 'User_Basket/User_Basket.html', {'app_name': 'User_Basket'})

def add_to_session_basket(request, product_id):
    basket = request.session.get('basket', {})
    basket[str(product_id)] = basket.get(str(product_id), 0) + 1
    request.session['basket'] = basket
    return redirect('basket')

def add_to_db_basket(request, product_id):
    cart, _ = Cart.objects.get_or_create(user_id=request.user.id)
    item, created = CartItem.objects.get_or_create(cart_id=cart.id, product_id=product_id)
    if not created:
        item.quantity += 1
    item.save()
    return redirect('basket')

def add_to_basket(request, product_id):
    if request.user.is_authenticated:
        return add_to_db_basket(request, product_id)
    else:
        return add_to_session_basket(request, product_id)
    
def basket_view(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user_id=request.user.id).first()
        items = CartItem.objects.filter(cart_id=cart.id) if cart else []
        total = sum(item.product.price * item.quantity for item in items)
        return render(request, 'basket.html', {'items': items, 'db_mode': True, 'total': total})
    else:
        basket = request.session.get('basket', {})
        items = []
        total = 0
        for product_id, quantity in basket.items():
            product = Product.objects.get(id=product_id)
            items.append({'product': product, 'quantity': quantity})
            total += product.price * quantity
        return render(request, 'basket.html', {'items': items, 'db_mode': False, 'total': total})
