from django.shortcuts import render
from Product_List.models import Product
from django.db.models import Max

def home(request):

    # 1) Build dynamic categories WITH image + name
    categories = (
        Product.objects
        .values('type')
        .annotate(image_url=Max('image_url'))  # get 1 image per category
        .order_by('type')
    )

    # 2) Featured = highest-priced, active products
    featured_products = Product.objects.filter(active=True).order_by('-price')[:6]

    return render(request, "Home_Page/Home_Page.html", {
        "categories": categories,
        "featured_products": featured_products,
    })
