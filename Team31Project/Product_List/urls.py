from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="products"),
    path("<int:pk>/", views.product_detail, name="product_detail"),
    path("<int:pk>/add/", views.add_to_basket, name="add_to_basket"),
    path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
]

