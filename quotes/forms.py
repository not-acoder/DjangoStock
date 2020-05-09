from django import forms
from .models import stonk 

class StonkForm(forms.ModelForm):
	class Meta:
		model=stonk
		fields=["ticker"]