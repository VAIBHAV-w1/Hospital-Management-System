from django.shortcuts import render
from datetime import date
from django.contrib.auth.hashers import make_password, check_password
from .models import CustomUser
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Appointment
from .models import Doctor
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, get_user_model
from django.db import IntegrityError, connection
from django.contrib.auth.hashers import make_password
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from .models import CustomUser
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.decorators import login_required
from .models import CustomUser

def index(request):
    return render(request, 'index.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser  # Import your CustomUser model

import re
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import CustomUser  # Assuming CustomUser is your user model

def is_valid_username(username):
    # Example validation: Username must contain only alphanumeric characters
    return bool(re.match('^[a-zA-Z0-9]+$', username))

def is_valid_password(password):
    # Example validation: Password must be at least 8 characters long
    return len(password) >= 8

def register(request):
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Validate username
        if not is_valid_username(username):
            messages.error(request, 'Invalid username format.')
            return redirect('register')

        # Validate email
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, 'Invalid email address.')
            return redirect('register')

        # Validate password
        if not is_valid_password(password):
            messages.error(request, 'Password must be at least 8 characters long.')
            return redirect('register')

        # Check if username or email already exists
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('register')

        # Create user
        try:
            # Create user object but don't save it yet
            user = CustomUser(username=username, email=email)
            user.set_password(password)  # set_password hashes the password before saving
            user.save()  # Now save the user object to the database
            messages.success(request, 'User registered successfully!')
            return redirect('success')
        except Exception as e:
            messages.error(request, 'An error occurred. Please try again.')
            return redirect('register')

    # If it's a GET request or form submission failed, render the registration form
    return render(request, 'register.html')

def log(request):
    if request.method == 'POST':
        # Introducing SQL injection vulnerability by directly concatenating strings
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Vulnerable point: directly concatenating strings into the query
        query = f"SELECT * FROM Hospital_customuser WHERE username = '{username}' AND password = '{password}'"

        with connection.cursor() as cursor:
            cursor.execute(query)
            row = cursor.fetchone()

        if row:
            return redirect('index')
        
        return render(request, 'log.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'log.html')

def index(request):
    doctors = Doctor.objects.all()
    return render(request, 'index.html', {'doctors': doctors})

def appointment_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        department = request.POST.get('department')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Create a new Appointment instance and save it to the database
        appointment = Appointment.objects.create(
            name=name,
            email=email,
            date=date,
            department=department,
            phone=phone,
            message=message
        )

        # Redirect to the success page after successfully creating the appointment
        return redirect('success')
        # 'success' should be the name or path of your success.html template or URL pattern

    else:
        return render(request, 'index.html')

def success_view(request):
    return render(request, 'success.html')

def latest_appointment_api(request):
    print("hhhhhhhhhhhhhhh")
    try:
        # Check if there's any data in the Appointment model
        if Appointment.objects.exists():
            # Fetch the latest appointment from the database    
            latest_appointment = Appointment.objects.latest('id')
            print("latest",latest_appointment)
            
            # Prepare data to be sent as JSON
            appointment_data = {
                'patientName': latest_appointment.name,
                'appointmentDate': str(latest_appointment.date),
                'services': ['Consultation', 'Treatment'],  # Replace with actual services
                'totalCost': 150.00,  # Replace with actual cost
            }

            return JsonResponse(appointment_data)
        else:
            return JsonResponse({'error': 'No appointments found.'}, status=404)

    except ObjectDoesNotExist:
        return JsonResponse({'error': 'No appointments found.'}, status=404)

def doctor_dashboard(request):
    
    doctor_appointments_data = [
        {
            'date': 'March 15, 2024',
            'patient': 'Jane Doe',
            'time': '2:30 PM - 3:00 PM',
            'location': 'Medical Center, Room 203',
        },
        {
            'date': 'March 20, 2024',
            'patient': 'John Smith',
            'time': '10:00 AM - 11:00 AM',
            'location': 'Health Clinic, Room 105',
        },
   
    ]

    return render(request, 'doctor_dashboard.html', {'appointments': doctor_appointments_data})

def doctor_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        query = f"SELECT * FROM Hospital_customuser WHERE username = '{username}'"

        with connection.cursor() as cursor:
            cursor.execute(query)
            row = cursor.fetchone()

        if row:
            # Check if the password is encrypted
            if row[1].startswith('pbkdf2_'):  # Assuming password is at index 1, adjust if needed
                # Password is encrypted, use Django's check_password function
                if check_password(password, row[1]):
                    # Redirect to a success page.
                    return redirect('index')
            else:
                # Password is not encrypted, bypass password check
                # Redirect to a success page.
                return redirect('index')
        
        # Return an 'invalid login' error message.
        return render(request, 'log.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'log.html')
    
class AppointmentsApiView(View):
    def get(self, request, *args, **kwargs):
        appointments = Appointment.objects.all()
        appointments_data = [
            {
                'name': appointment.name,
                'email': appointment.email,
                'date': appointment.date.strftime('%B %d, %Y'),  # Format date as needed
                'department': appointment.department,
                'phone': appointment.phone,
                'message': appointment.message,
            }
            for appointment in appointments
        ]
        return JsonResponse(appointments_data, safe=False)

from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST

@require_POST
@csrf_exempt
@login_required
def change_email(request):
    new_email = request.POST.get('new_email')

    if not new_email:
        return JsonResponse({'success': False, 'message': 'New email address is required.'})

    try:
        # Assuming you have a custom user model, replace 'User' with your user model
        user = request.user
        user.email = new_email
        user.save()
        return JsonResponse({'success': True, 'message': 'Email address changed successfully.'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Error changing email: {str(e)}'})

def about_view(request):
    return render(request, 'about.html')

def doctors_view(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors.html', {'doctors': doctors})

def news_view(request):
    return render(request, 'news.html')

def contact_view(request):
    return render(request, 'contact.html')

def appointments_view(request):
    all_appointments = Appointment.objects.all()
    today = date.today()
    upcoming = []
    completed = []
    
    for appt in all_appointments:
        if appt.date >= today:
            upcoming.append(appt)
        else:
            completed.append(appt)
            
    return render(request, 'appointments.html', {'upcoming': upcoming, 'completed': completed})