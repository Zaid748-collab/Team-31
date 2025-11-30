from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.hashers import make_password

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data["password"])
            user.save()
            return redirect("/")  # go to home or whatever you choose
    else:
        form = SignupForm()

    return render(request, "Sign_Up/Sign_Up.html", {"form": form})
