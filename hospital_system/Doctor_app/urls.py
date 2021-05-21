from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.DoctorHome, name='DoctorHome'),
    path('Doctor_Signin',views.Doctor_Signin, name='Doctor_Signin'),
    path('Doctor_Signup',views.Doctor_Signup, name='Doctor_Signup'),
    path('DoctorExtra',views.Doctor_Extra, name='DoctorExtra'),
    path('Doctor_done',views.Doctor_done, name='Doctor_done'),
    path('Doctor_Prescription',views.Doctor_Prescription, name='Doctor_Prescription'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'Doctor_app/password_reset_confirm.html') , name = 'password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'Doctor_app/password_reset_complete.html') , name = 'password_reset_complete'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name = 'Doctor_app/password_reset.html') , name = 'password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'Doctor_app/password_reset_done.html') , name = 'password_reset_done'),

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)