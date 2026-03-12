from django.shortcuts import render
from Product_List.models import Product
from django.db.models import Max
from django.db.models import Case, When
def home(request):
    
    categories = (
        Product.objects
        .values('type')
        .annotate(image_url=Max('image_url'))
        .order_by('type')
    )

    featured_products = Product.objects.filter(active=True).order_by('-price')[:6]
    recent_ids = request.session.get("recently_viewed", [])

    preserved_order = Case(*[
        When(id=pk, then=pos) for pos, pk in enumerate(recent_ids)
    ])

    recently_viewed_products = (
        Product.objects.filter(id__in=recent_ids, active=True)
        .order_by(preserved_order)
    )
    return render(request, "Home_Page/Home_Page.html", {
        "categories": categories,
        "featured_products": featured_products,
        "recently_viewed_products": recently_viewed_products,
    })
