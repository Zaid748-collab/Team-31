from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="Sign_Up/signup.html"), name="signup"),
]
