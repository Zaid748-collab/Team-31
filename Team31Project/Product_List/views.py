from django.shortcuts import render

def index(request):
    return render(request, 'Product_List/Product_List.html', {'app_name': 'Product_List'})