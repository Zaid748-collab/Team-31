from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserForm

def profile_view(request):
    if not request.user.is_authenticated:
        return render(request, "base.html", {"not_logged_in": True})
    else:
        return render(request, "Profile/profile.html", {"user": request.user})


def edit_profile(request):
    user = request.user
    old_email = user.email

    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            updated_user = form.save(commit=False)

            # Reset email_verified if email changed
            if form.cleaned_data["email"] != old_email:
                updated_user.email_verified = False

            updated_user.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")
    else:
        form = UserForm(instance=user)

    return render(request, "Profile/profile_edit.html", {"form": form})


from django.http import JsonResponse
from django.contrib.auth import authenticate, login

def custom_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "error": "Invalid username or password."})
    return JsonResponse({"success": False, "error": "Invalid request."})