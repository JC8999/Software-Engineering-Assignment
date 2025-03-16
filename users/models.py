from django.contrib.auth.models import AbstractUser, Group
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ("Client", "Client"),
        ("Lawyer", "Lawyer"),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="Client")
    phone_number = models.CharField(max_length=15, unique=True)

    def assign_group(self):
        """Assign the user to the correct group based on role."""
        group_name = self.role
        group, created = Group.objects.get_or_create(name=group_name) # Checks if group exists and creates it if not
        self.groups.add(group)

    def save(self, *args, **kwargs):
        """Override save method to assign user to a group based on role."""
        super().save(*args, **kwargs)
        self.assign_group()  # Assign group after saving

    def __str__(self):
        return self.get_full_name()
