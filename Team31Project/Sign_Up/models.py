from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    profile_picture_url = models.TextField(null=True, blank=True)
    gender = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=1000, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    email_verified = models.BooleanField(default=False)

    class Meta:
        db_table = 'User'