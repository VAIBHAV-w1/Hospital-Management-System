from django.contrib import admin
from .models import CustomUser, Doctor, User, Appointment

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'user_type']
    search_fields = ['username', 'email']

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialty', 'password']
    search_fields = ['name', 'specialty']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_doctor']
    search_fields = ['username', 'email']
    list_filter = ['is_doctor']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'date', 'department', 'phone']
    search_fields = ['name', 'email']
    list_filter = ['department', 'date']
