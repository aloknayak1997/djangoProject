from django import forms
from .import models

class User_form(forms.ModelForm):
    class Meta:
        model = models.DpyTable
        fields = ['username','password'] 


