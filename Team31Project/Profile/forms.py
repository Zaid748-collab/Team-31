from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "date_of_birth",
            "phone_number",
            "gender",
            "profile_picture_url",
        ]
