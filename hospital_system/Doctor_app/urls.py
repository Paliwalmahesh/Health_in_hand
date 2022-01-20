from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# from django.conf.urls import re_path

urlpatterns = [
   
   
   
    path('logout_view',views.logout_view, name='logout_view'),
    path('',views.DoctorHome, name='DoctorHome'),
    path('View_Lab_report_Doc/<str:pk>',views.View_Lab_report_Doc, name='View_Lab_report_Doc'),
    path('View_Prescription_Doc/<str:pk>',views.View_Prescription_Doc, name='View_Prescription_Doc'),
    path('updateDoctorExtraForm_c/<str:username>',views.updateDoctorExtraForm_c, name='updateDoctorExtraForm_c'),
    path('Doctor_Signin',views.Doctor_Signin, name='Doctor_Signin'),
    path('Doctor_Signup',views.Doctor_Signup, name='Doctor_Signup'),
    path('Doctor_done',views.Doctor_done, name='Doctor_done'),
    path('Heart_health',views.Heart_health, name='Heart_health'),
    path('View_Prescription',views.View_Prescription, name='View_Prescription'),
    path('View_Reports',views.View_Reports, name='View_Reports'),
    path('Doctor_Prescription',views.Doctor_Prescription, name='Doctor_Prescription'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'Doctor_app/password_reset_confirm.html') , name = 'password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'Doctor_app/password_reset_complete.html') , name = 'password_reset_complete'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name = 'Doctor_app/password_reset.html') , name = 'password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'Doctor_app/password_reset_done.html') , name = 'password_reset_done'),
    path('updateDoctorExtraForm/',views.updateDoctorExtraForm, name='updateDoctorExtraForm'),

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)