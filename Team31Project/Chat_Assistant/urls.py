from django.urls import path
from . import views

urlpatterns = [
    path("respond/", views.chat_respond, name="chat_respond"),
]
