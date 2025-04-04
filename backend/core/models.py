#from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=255, default="Unknown")  # Add a default value
    age = models.IntegerField()
    gender = models.CharField(max_length=10, default='Male')
    contact = models.CharField(max_length=15, unique=True, default="N/A")
    address = models.TextField()

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    contact = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')])

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name} ({self.date})"

class Scan(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    scan_type = models.CharField(max_length=50,default="Unknown")
    image = models.ImageField(upload_to='scans/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.scan_type} - {self.patient.name}"

class Report(models.Model):
    scan = models.OneToOneField(Scan, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report for {self.scan.patient.name}"
