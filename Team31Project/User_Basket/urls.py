from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:product_id>/', views.add_to_basket, name='add_to_basket'),
    path('remove/<int:product_id>/', views.remove_from_basket, name='remove_from_basket'),
    path('basket/', views.basket_view, name='basket'),
]