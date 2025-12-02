from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home_Page.urls')),
    path('about/', include('About_Us.urls')),
    path('contact/', include('Contact_Us.urls')),
    path('products/', include('Product_List.urls')),
    path('signup/', include('Sign_Up.urls')),
    path('basket/', include('User_Basket.urls')),
    path('orders/', include('Previous_Orders.urls')),
    path('checkout/', include('Checkout.urls')),
    path('profile/', include('Profile.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='Sign_Up/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
