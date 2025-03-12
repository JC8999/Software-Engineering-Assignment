from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_lawyer = models.BooleanField(default=False) # Differentiates between lawyer and client users
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.get_full_name()
