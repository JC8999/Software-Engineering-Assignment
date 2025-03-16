from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'role', 'is_staff')
    list_filter = ('groups', 'is_staff', 'is_superuser')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'phone_number')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'phone_number', 'role', 'password1', 'password2')}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)