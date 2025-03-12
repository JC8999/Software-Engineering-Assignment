from django.db import models
from users.models import CustomUser
from lawyers.models import LawyerProfile

class Appointment(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
    ]

    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="appointments")
    lawyer = models.ForeignKey(LawyerProfile, on_delete=models.CASCADE, related_name="appointments")
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    cancellation_reason = models.TextField(blank=True, null=True)

    class Meta:
        constraints = [
            # Prevent duplicate bookings for a lawyer at the same time
            models.UniqueConstraint(fields=["lawyer", "date", "time"], name="unique_appointment"),
        ]

    def __str__(self):
        return f"{self.client.get_full_name()} - {self.lawyer.user.get_full_name()} on {self.date} at {self.time} [{self.get_status_display()}]"
