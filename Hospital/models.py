from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    )

    user_type = models.CharField(max_length=15, choices=USER_TYPE_CHOICES, default='patient')
    is_doctor = models.BooleanField(default=False)  # New field to identify whether the user is a doctor

    # Additional fields for non-doctor users can be added here

class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    password = models.CharField(max_length=50, default='some_default_value')
    image = models.ImageField(upload_to='doctors/')

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    is_doctor = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Appointment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    date = models.DateField()
    department_choices = [
        ('general_health', 'General Health'),
        ('cardiology', 'Cardiology'),
        ('dental', 'Dental'),
        ('medical_research', 'Medical Research'),
    ]
    department = models.CharField(max_length=50, choices=department_choices)
    phone = models.CharField(max_length=15)
    message = models.TextField()

   

