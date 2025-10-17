from django.shortcuts import render

def index(request):
    return render(request, 'Sign_Up/Sign_Up.html', {'app_name': 'Sign_Up'})