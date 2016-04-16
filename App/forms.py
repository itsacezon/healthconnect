from django import forms
from .models import Doctor

class InputForm(forms.ModelForm):
	class Meta:
		model = Doctor 
		fields = [
			"__all__"
		]
