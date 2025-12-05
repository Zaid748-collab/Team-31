from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="products"),
    path("<int:pk>/", views.product_detail, name="product_detail"),
    path("<int:pk>/add/", views.add_to_basket, name="add_to_basket"),
]
