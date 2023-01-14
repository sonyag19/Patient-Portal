from django.db import models
from datetime import datetime

# Create your models here.

doctor_list = (
    ('Dr.Sudha Murthy','DR.SUDHA MURTHY'),
    ('Dr.Ragupathi', 'DR.RAGUPATHI'),
    ('Dr.Lee','DR.LEE'),
)

department=(
    ('Pediatricians','Pediatricians'),
    ('Neurologists','Neurologists'),
    ('Obstetricians and gynecologists','Obstetricians and gynecologists'),
    ('General Physician','General Physician'),
    ('Cardiologists','Cardiologists')
)

TIME_CHOICES = (
    ("10 AM", "10 AM"),
    ("10:30 AM", "10:30 AM"),
    ("11 AM", "11 AM"),
    ("11:30 AM", "11:30 AM"),
    ("3 PM", "3 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5 PM", "5 PM"),
    ("5:30 PM", "5:30 PM"),
)

class SignUpModel(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    email=models.EmailField()
    password = models.CharField(max_length=20)
    cpassword = models.CharField(max_length=20)
    doctor=models.CharField(max_length=20, choices=doctor_list, default='')
    date=models.DateField()
    addr1=models.CharField(max_length=20)
    addr2=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    zip=models.IntegerField()
    phone=models.IntegerField()
    photo=models.FileField(upload_to='PP_app/static')

class newAppointment(models.Model):
    depart=models.CharField(max_length=100,choices=department,default='')
    doctor=models.CharField(max_length=20,choices=doctor_list,default='')
    apptDate=models.DateField()
    apptTime=models.TimeField()
    appointment_description=models.CharField(max_length=150)
