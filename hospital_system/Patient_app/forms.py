from django import forms
from .models import PatientPasscodes,PatientExtra


class PatientExtraForm(forms.ModelForm):
	class Meta:
		model = PatientExtra
		fields = ['mobile','Profilephoto']
		widgets = {
			'mobile' : forms.TextInput(attrs={'class':'form-control my-2'}),
			'Profilephoto' :forms.FileInput(attrs={'class':'form-control my-4'}),
			
		  
		}
class PatientPasscodesForm(forms.ModelForm):
	class Meta:
		model = PatientPasscodes
		fields = ['passcode']
		widgets = {
			'mobile' : forms.TextInput(attrs={'class':'form-control my-2'}),
			
			
		  
		}
