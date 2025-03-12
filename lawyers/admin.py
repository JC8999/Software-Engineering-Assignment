from django.contrib import admin
from .models import LawyerProfile, UnavailableTimeSlot

class LawyerProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "practice_area", "available_from", "available_to")
    list_filter = ("practice_area",)
    search_fields = ("user__username", "user__email")

class UnavailableTimeSlotAdmin(admin.ModelAdmin):
    list_display = ("lawyer", "date", "start_time", "end_time")
    list_filter = ("date", "lawyer")
    search_fields = ("lawyer__user__username", "lawyer__user__email")

admin.site.register(LawyerProfile, LawyerProfileAdmin)
admin.site.register(UnavailableTimeSlot, UnavailableTimeSlotAdmin)