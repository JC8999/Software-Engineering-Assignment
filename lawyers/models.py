from django.core.exceptions import ValidationError
from django.db import models
from users.models import CustomUser

PRACTICE_AREAS = [
    ("civil", "Civil Law"),
    ("criminal", "Criminal Law"),
    ("corporate", "Corporate Law"),
    ("administrative", "Administrative Law"),
]

class LawyerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    practice_area = models.CharField(max_length=20, choices=PRACTICE_AREAS)
    available_from = models.TimeField()
    available_to = models.TimeField()

    def clean(self):
        """Ensures only users in the lawyer group can have a LawyerProfile."""
        if not self.user.groups.filter(name="Lawyer").exists():
            raise ValidationError("User must be in the 'Lawyer' group to be assigned a Lawyer Profile.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.get_practice_area_display()} - {self.user.phone_number}"
    
class UnavailableTimeSlot(models.Model):
    lawyer = models.ForeignKey(LawyerProfile, on_delete=models.CASCADE, related_name="unavailable_slots")
    date = models.DateField()  # Specific date of unavailability
    start_time = models.TimeField()  # Start of unavailability
    end_time = models.TimeField()  # End of unavailability

    def __str__(self):
        return f"{self.lawyer.user.get_full_name()} - Unavailable {self.date} {self.start_time} to {self.end_time}"