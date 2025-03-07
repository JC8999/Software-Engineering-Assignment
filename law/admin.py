from django.contrib import admin
from .models import CustomUser, TimeSlot, Appointment

# Register your models here.
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('lawyer', 'date', 'start_time', 'end_time', 'is_booked')
    list_filter = ('lawyer', 'date', 'is_booked')
    ordering = ('date', 'start_time')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('client', 'time_slot', 'status')
    list_filter = ('status', 'time_slot__lawyer', 'time_slot__date')
    ordering = ('time_slot__date', 'time_slot__start_time')

admin.site.register(CustomUser)
admin.site.register(TimeSlot, TimeSlotAdmin)
admin.site.register(Appointment, AppointmentAdmin)

