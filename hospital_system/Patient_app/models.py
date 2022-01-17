from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Address(models.Model):
    Place_name=models.CharField(max_length=12,blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(default="India",max_length=12,blank=True)
    pincode= models.IntegerField(null=True, blank=True)

class PatientExtra(models.Model):  
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    joindate=models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=12)
    Profilephoto = models.ImageField(default='default.png',null=True, blank=True)
    Address=models.OneToOneField(Address,on_delete=models.CASCADE, null=True ,blank=True)
    def __str__(self):
        return self.user.username
   

class PatientPasscodes(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    passcode=models.CharField(max_length=10, null = True)
    def __str__(self):
        return self.user.username




