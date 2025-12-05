from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    date_of_birth = forms.DateField(
        widget=forms.SelectDateWidget(years=range(1900, 2026)),
        required=False
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
            "date_of_birth",
            "phone_number",
            "gender",
            "profile_picture",
        ]
    