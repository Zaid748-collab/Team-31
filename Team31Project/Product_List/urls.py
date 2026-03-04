from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="products"),
    path("<int:pk>/", views.product_detail, name="product_detail"),
    path("<int:pk>/add/", views.add_to_basket, name="add_to_basket"),

    path("wishlist/add/<int:product_id>/", views.add_to_wishlist, name="add_to_wishlist"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path("wishlist/remove/<int:item_id>/", views.remove_from_wishlist, name="remove_from_wishlist"),
    path("reviews/<int:product_id>/submit/", views.submit_review, name="submit_review"),
]