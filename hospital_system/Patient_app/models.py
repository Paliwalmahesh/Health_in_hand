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
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class PatientPasscodes(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    passcode=models.CharField(max_length=10, null = True)
    
    def __str__(self):
        return self.user.username

class Medical_details(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    age=models.IntegerField(null=True,blank=True)
    Gender=models.CharField(max_length=6,null=True,blank=True)
    cp=models.IntegerField(null=True,blank=True)
    trestbps=models.IntegerField(null=True,blank=True)
    cholesterol=models.IntegerField(null=True,blank=True)
    restecg=models.IntegerField(null=True,blank=True)
    thalach=models.IntegerField(null=True,blank=True)
    exang=models.BooleanField(null=True,blank=True)
    fbs=models.BooleanField(null=True,blank=True)
    oldpeak=models.FloatField(null=True,blank=True)
    slope=models.IntegerField(null=True,blank=True)
    ca=models.IntegerField(null=True,blank=True)
    thal=models.IntegerField(null=True,blank=True)
    target=models.IntegerField(null=True,blank=True)


