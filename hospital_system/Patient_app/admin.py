from django.contrib import admin
from .models import PatientExtra,Address,PatientPasscodes

# Register your models here.
admin.site.register(PatientExtra)
admin.site.register(Address)

admin.site.register(PatientPasscodes)