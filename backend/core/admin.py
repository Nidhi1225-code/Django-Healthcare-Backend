from django.contrib import admin
from .models import Patient,Doctor,Appointment,Scan,Report

admin.site.register(Patient)
admin.site.register(Scan)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Report)

# Register your models here.
