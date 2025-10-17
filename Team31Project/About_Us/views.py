from django.shortcuts import render

def index(request):
    return render(request, 'About_Us/About_Us.html', {'app_name': 'About_Us'})