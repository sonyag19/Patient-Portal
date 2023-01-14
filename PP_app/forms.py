from django import forms
from .models import *

class SignUpForm(forms.ModelForm):
    class Meta:
        model=SignUpModel
        fields="__all__"

class Loginform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=20)

class NewAppointmentForm(forms.ModelForm):
    class Meta:
        model=newAppointment
        fields="__all__"


    # depart = forms.CharField(max_length=100, choices=department, default='')
    # doctor = forms.CharField(max_length=20, choices=doctor_list, default='')
    # apptDate = forms.DateField()
    # apptTime = forms.TimeField()
    # appointment_description = forms.CharField(max_length=150)