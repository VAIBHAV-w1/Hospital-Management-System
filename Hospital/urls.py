"""
URL configuration for PracticeHosp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from .import views
from .views import register, log, doctor_dashboard, doctor_login, change_email
from .views import appointment_view, AppointmentsApiView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', register, name='register'),
    path('register/log/', log, name='log'),
    path('appointment/',views.appointment_view, name='appointment_view'),
    path('index/success/', views.success_view, name='success'),
    path('api/latest_appointment/', views.latest_appointment_api, name='latest_appointment_api'),
    path('doctor_dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('login/doctor_login/', views.doctor_login, name='doctor_login'),
    path('api/appointments/', AppointmentsApiView.as_view(), name='appointments-api'),
    path('accounts/change-email/', LoginView.as_view(), name='change_email'),
    path('about/', views.about_view, name='about'),
    path('doctors/', views.doctors_view, name='doctors'),
    path('news/', views.news_view, name='news'),
    path('contact/', views.contact_view, name='contact'),
    path('appointments/', views.appointments_view, name='appointments'),
]
