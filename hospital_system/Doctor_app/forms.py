from django.forms import ModelForm
from .models import DoctorExtra
from django import forms
from Patient_app.models import Address


class DoctorExtraForm(ModelForm):
	class Meta:
		model = DoctorExtra
		fields = ['mobile','Profilephoto']
		widgets = {
			'mobile' : forms.TextInput(attrs={'class':'form-control my-2'}),
			'Profilephoto' :forms.FileInput(attrs={'class':'form-control my-2'}),
			
		  
		}

class AddressForm(ModelForm):
	class Meta:
		model = Address
		fields = '__all__'
		widgets = {
			'Place_name' : forms.TextInput(attrs={'class':'form-control my-2'}),
			'city' : forms.TextInput(attrs={'class':'form-control my-2'}),
			'state' : forms.TextInput(attrs={'class':'form-control my-2'}),
			'country' : forms.TextInput(attrs={'class':'form-control my-2'}),
			'pincode' : forms.NumberInput(attrs={'class':'form-control my-2'}),
		  
		}
		