from django.contrib.auth.models import AbstractUser, Group
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ("Client", "Client"),
        ("Lawyer", "Lawyer"),
        ("Admin", "Admin"),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="Client")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)

    def assign_group(self):
        """Assigns users to the correct group based on role, but keeps superusers out of a group by giving them an admin role."""
        self.groups.clear()  # Resets group assignments to clear superusers

        if self.is_superuser:
            self.role = "Admin"  # Automatically set superusers as "Admin". This is a role not a group.
        elif self.role == "Client":
            client_group, _ = Group.objects.get_or_create(name="Client")
            self.groups.add(client_group)
        elif self.role == "Lawyer":
            lawyer_group, _ = Group.objects.get_or_create(name="Lawyer")
            self.groups.add(lawyer_group)

    def save(self, *args, **kwargs):
        """Override save method to assign user to a group based on role."""
        super().save(*args, **kwargs)  # Save the user first to prevent errors with updating fields
        self.assign_group() # Assign group after saving
        super().save(update_fields=["role"])

    def __str__(self):
        return self.get_full_name()
