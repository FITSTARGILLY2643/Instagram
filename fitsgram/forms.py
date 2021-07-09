from django import forms
from .models import Image,Comment,Profile

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user','profile','likes','pub_date']
