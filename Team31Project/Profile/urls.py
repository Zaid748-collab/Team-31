from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Profile routes
    path('', views.profile_view, name='profile'),
    path('edit/', views.edit_profile, name='profile_edit'),

    # Custom login route for popup
    path("login/custom/", views.custom_login, name="custom_login"),

    # Password change routes
    path("password/",
         auth_views.PasswordChangeView.as_view(template_name="Profile/change_password.html"),
         name="password_change"),
    path("password/done/",
         auth_views.PasswordChangeDoneView.as_view(template_name="Profile/change_password_done.html"),
         name="password_change_done"),
]