from django.contrib import admin
from .models import DoctorExtra,Prescription

# Register your models here.
admin.site.register(Prescription)
admin.site.register(DoctorExtra)
