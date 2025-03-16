from django.contrib import admin
from django.contrib.auth.models import Group
from .models import LawyerProfile, UnavailableTimeSlot

class LawyerProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "practice_area", "available_from", "available_to")
    list_filter = ("practice_area",)
    search_fields = ("user__username", "user__email")

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """Filter user selection to only show users in the 'Lawyer' group."""
        if db_field.name == "user":
            lawyer_group = Group.objects.get(name="Lawyer")
            kwargs["queryset"] = lawyer_group.user_set.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class UnavailableTimeSlotAdmin(admin.ModelAdmin):
    list_display = ("lawyer", "date", "start_time", "end_time")
    list_filter = ("date", "lawyer")
    search_fields = ("lawyer__user__username", "lawyer__user__email")

admin.site.register(LawyerProfile, LawyerProfileAdmin)
admin.site.register(UnavailableTimeSlot, UnavailableTimeSlotAdmin)