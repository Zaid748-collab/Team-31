from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()

def profile_view(request):
    user = request.user if request.user.is_authenticated else None
    context = {
        'user': user,
    } 
    return render(request, 'profile/profile.html', context)