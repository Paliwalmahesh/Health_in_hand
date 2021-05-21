from django.db import models
from django.contrib.auth.models import User
from Patient_app.models import Address
from PIL import Image

# Create your models here.
class DoctorExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    joindate=models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=12)
    Profilephoto = models.ImageField(default='default.png' ,upload_to='profile_pics', null=True, blank=True)
    Address=models.OneToOneField(Address,on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.user.username



class Prescription(models.Model):
    Doctor_name=models.ForeignKey(User, on_delete=models.CASCADE,related_name='Doctor_name')
    Patient_name=models.ForeignKey(User, on_delete=models.CASCADE,related_name='Patient_name')
    Prescription_date=models.DateTimeField(auto_now_add=True)
    Prescription_text=models.TextField(null=True, blank=True)
   
    special_advice =models.TextField(null=True, blank=True)
    def __str__(self):
        Prescription_date_c=str(self.Prescription_date)
        return Prescription_date_c
