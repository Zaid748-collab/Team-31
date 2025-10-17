from django.shortcuts import render

def index(request):
    return render(request, 'Home_Page/Home_Page.html', {'app_name': 'Home_Page'})