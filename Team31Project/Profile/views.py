from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileForm

User = get_user_model()
@login_required
def profile_view(request):
    user = request.user if request.user.is_authenticated else None
    context = {
        'user': user,
    } 
    return render(request, 'profile/profile.html', context)
@login_required
def edit_profile(request):
    user = request.user
    old_email = user.email

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            updated_user = form.save(commit=False)

            # if email changed → set email_verified to False
            if form.cleaned_data["email"] != old_email:
                updated_user.email_verified = False

            updated_user.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")   # back to view page
    else:
        # pre-fill with current values
        form = ProfileForm(instance=user)

    return render(request, "Profile/Profile_edit.html", {"form": form})