from django.contrib import admin
from django.urls import path, include

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
]
