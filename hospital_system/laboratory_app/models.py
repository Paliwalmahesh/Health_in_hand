from django.db import models
from django.contrib.auth.models import User
from Patient_app.models import Address
from PIL import Image

# Create your models here.
class LaboratoryExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    joindate=models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=12)
    Profilephoto = models.ImageField(null=True,blank=True)
    Address=models.OneToOneField(Address,on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.user.username



class Lab_report(models.Model):
    Lab_reportid = models.AutoField(primary_key=True)
    Laboratory_name=models.ForeignKey(User, on_delete=models.CASCADE,related_name='Laboratory_name')
    Doctor_name=models.ForeignKey(User, on_delete=models.CASCADE,related_name='Lab_Doctor_name')
    Patient_name=models.ForeignKey(User, on_delete=models.CASCADE,related_name='Lab_Patient_name')
    report_date=models.DateTimeField(auto_now_add=True)
    Test_name=models.CharField(max_length=50,null=True, blank=True)
    report_text=models.TextField(null=True, blank=True)
    def __str__(self):
        Prescription_date_c=str(self.report_date)
        return Prescription_date_c
# Create your models here.
