from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.LaboratoryHome, name='LaboratoryHome'),
    path('Laboratory_Signin',views.Laboratory_Signin, name='Laboratory_Signin'),
    path('Laboratory_Signup',views.Laboratory_Signup, name='Laboratory_Signup'),
    # path('LaboratoryExtra',views.Laboratory_Extra, name='LaboratoryExtra'),
    path('Laboratory_done',views.Laboratory_done, name='Laboratory_done'),
    path('Laboratory_report',views.Laboratory_report, name='Laboratory_report'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)