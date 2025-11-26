from django.shortcuts import render

def index(request):
    return render(request, 'Profile/Profile.html', {'app_name': 'Profile'})