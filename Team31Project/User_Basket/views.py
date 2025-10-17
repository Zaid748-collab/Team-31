from django.shortcuts import render

def index(request):
    return render(request, 'User_Basket/User_Basket.html', {'app_name': 'User_Basket'})