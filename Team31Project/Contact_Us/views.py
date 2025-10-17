from django.shortcuts import render

def index(request):
    return render(request, 'Contact_Us/Contact_Us.html', {'app_name': 'Contact_Us'})