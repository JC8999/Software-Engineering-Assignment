from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('client', 'Client'),
        ('lawyer', 'Lawyer'),
    )

    PRACTICE_AREA_CHOICES = (
        ('civil', 'Civil'),
        ('criminal', 'Criminal'),
        ('administrative', 'Administrative'),
        ('corporate', 'Corporate'),
    )


    groups = models.ManyToManyField(Group, related_name="customuser_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions", blank=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    practice_area = models.CharField(max_length=15, choices=PRACTICE_AREA_CHOICES, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.user_type == 'client':  #Ensure clients don't have practice_area
            self.practice_area = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

class TimeSlot(models.Model):
    lawyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="time_slots", limit_choices_to={'user_type': 'lawyer'})
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_booked = models.BooleanField(default=False)  #True when a client books this slot

    def __str__(self):
        return f"{self.lawyer.username} - {self.date} {self.start_time} to {self.end_time}"

class Appointment(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="appointments", limit_choices_to={'user_type': 'client'})
    time_slot = models.OneToOneField(TimeSlot, on_delete=models.CASCADE, related_name="appointment")
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('canceled', 'Canceled')],
        default='pending'
    )
    notes = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.time_slot.is_booked:
            raise ValueError("This time slot is already booked.")
        self.time_slot.is_booked = True  #Mark slot as booked
        self.time_slot.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Appointment: {self.client.username} with {self.time_slot.lawyer.username} on {self.time_slot.date} at {self.time_slot.start_time}"

