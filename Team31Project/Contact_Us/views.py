from django.shortcuts import render

def contact(request):
    return render(request, "Contact_Us/Contact_Us.html")
