from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.PatientHome, name='PatientHome'),
    path('Patient_Signin',views.Patient_Signin, name='Patient_Signin'),
    path('Patient_Signup',views.Patient_Signup, name='Patient_Signup'),
    path('PatientExtra',views.Patient_Extra, name='PatientExtra'),
    path('Patient_done',views.Patient_done, name='Patient_done'),
    path('Patient_Prescription',views.Patient_Prescription, name='Patient_Prescription'),
    path('Patient_Report',views.Patient_Report, name='Patient_Report'),
    
    


] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)