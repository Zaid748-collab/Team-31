from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='basket'),
    path('', views.basket_view, name='basket'),
    path('add/<int:product_id>/', views.add_to_basket, name='add_to_basket'),
]