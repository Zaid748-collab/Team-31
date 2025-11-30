from django.urls import path
<<<<<<< Updated upstream
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="Sign_Up/signup.html"), name="signup"),
=======
from .views import signup_view

urlpatterns = [
    path('', signup_view, name='signup'),
>>>>>>> Stashed changes
]
