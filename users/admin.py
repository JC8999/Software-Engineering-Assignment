from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone_number', 'is_lawyer', 'is_staff')
    list_filter = ('is_lawyer', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'phone_number')

admin.site.register(CustomUser, CustomUserAdmin)
