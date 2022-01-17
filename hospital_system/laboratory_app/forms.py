from django import forms
from .models import LaboratoryExtra


class LaboratoryExtraForm(forms.ModelForm):
	class Meta:
		model = LaboratoryExtra
		fields = ['mobile','Profilephoto']
		widgets = {
			'mobile' : forms.TextInput(attrs={'class':'form-control my-2'}),
			'Profilephoto' :forms.FileInput(attrs={'class':'form-control my-2'}),
			
		  
		}