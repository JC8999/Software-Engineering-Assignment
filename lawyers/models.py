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
    bio = models.TextField()
    available_from = models.TimeField()
    available_to = models.TimeField()

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.get_practice_area_display()} - {self.user.phone_number}"
    
class UnavailableTimeSlot(models.Model):
    lawyer = models.ForeignKey(LawyerProfile, on_delete=models.CASCADE, related_name="unavailable_slots")
    date = models.DateField()  # Specific date of unavailability
    start_time = models.TimeField()  # Start of unavailability
    end_time = models.TimeField()  # End of unavailability

    def __str__(self):
        return f"{self.lawyer.user.get_full_name()} - Unavailable {self.date} {self.start_time} to {self.end_time}"