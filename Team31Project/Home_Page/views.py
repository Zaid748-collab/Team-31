from django.shortcuts import render
from Product_List.models import Product
from django.db.models import Max

def home(request):
    
    categories = (
        Product.objects
        .values('type')
        .annotate(image_url=Max('image_url'))
        .order_by('type')
    )

    featured_products = Product.objects.filter(active=True).order_by('-price')[:6]

    return render(request, "Home_Page/Home_Page.html", {
        "categories": categories,
        "featured_products": featured_products,
    })
