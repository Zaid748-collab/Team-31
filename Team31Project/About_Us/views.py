from django.shortcuts import render

def about(request):
    return render(request, "About_Us/About_Us.html")
