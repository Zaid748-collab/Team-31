# Sign_Up/views.py
from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = SignUpForm()
    return render(request, "Sign_Up/Sign_Up.html", {"form": form})