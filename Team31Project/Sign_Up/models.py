from django.db import models

class User(models.Model):
    username = models.CharField(max_length=1000, unique=True)
    email = models.CharField(max_length=1000, unique=True)
    password = models.CharField(max_length=1000)

    first_name = models.TextField()
    last_name = models.TextField()
    profile_picture_url = models.TextField(null=True, blank=True)
    gender = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=1000, null=True, blank=True)

    date_of_birth = models.DateField(null=True, blank=True)

    is_admin = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)

    class Meta:
        db_table = 'User'   # This maps to your existing PGAdmin table

    def __str__(self):
        return self.username
