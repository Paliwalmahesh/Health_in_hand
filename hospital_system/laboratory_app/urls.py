from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('View_Lab_report_Lab/<str:pk>',views.View_Lab_report_Lab, name='View_Lab_report_Lab'),
    path('View_Reports_lab',views.View_Reports_lab, name='View_Reports_lab'),
    path('',views.LaboratoryHome, name='LaboratoryHome'),
    path('updateLaboratoryExtraForm_c/<str:username>',views.updateLaboratoryExtraForm_c, name='updateLaboratoryExtraForm_c'),
    path('updateLaboratoryExtraForm',views.updateLaboratoryExtraForm, name='updateLaboratoryExtraForm'),
    path('Laboratory_Signin',views.Laboratory_Signin, name='Laboratory_Signin'),
    path('Laboratory_Signup',views.Laboratory_Signup, name='Laboratory_Signup'),
    path('Laboratory_done',views.Laboratory_done, name='Laboratory_done'),
    path('Laboratory_report',views.Laboratory_report, name='Laboratory_report'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)