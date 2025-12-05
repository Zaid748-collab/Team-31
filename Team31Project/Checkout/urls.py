from django.urls import path
from .views import checkout_view, confirm_checkout

urlpatterns = [
    path("", checkout_view, name="checkout"),
    path("confirm/", confirm_checkout, name="confirm_checkout"),
]
