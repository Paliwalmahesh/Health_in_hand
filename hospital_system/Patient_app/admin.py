from django.contrib import admin
from .models import PatientExtra,Address,Medical_details

# Register your models here.
admin.site.register(PatientExtra)
admin.site.register(Address)
admin.site.register(Medical_details)