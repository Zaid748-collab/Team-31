from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "date_of_birth",      # or date_of_birth
            "phone_number",
            "gender",
            "profile_picture_url",
        ]
