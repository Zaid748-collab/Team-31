from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm

@login_required
def profile_view(request):
    return render(request, "Profile/profile.html", {"user": request.user})

@login_required
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