# Team31Project/Home_Page/urls.py
from django.urls import path
from .views import home

urlpatterns = [
    path("", home, name="home"),
]
