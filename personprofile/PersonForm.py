from django import forms
from .models import Person

class PersonForm(forms.Form):
    name = forms.CharField(required=False, label='Name')
    email = forms.EmailField(required=False, label='Email')