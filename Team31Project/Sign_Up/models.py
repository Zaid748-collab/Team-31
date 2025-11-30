from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    profile_picture_url = models.URLField(null=True, blank=True)

    is_admin = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)

    class Meta:
        db_table = 'User'   # IMPORTANT! Use your existing PGAdmin table

    def __str__(self):
        return self.username
