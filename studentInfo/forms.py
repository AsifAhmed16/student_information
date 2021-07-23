from django import forms
from .models import *


class StudentInformationForm(forms.ModelForm):
    class Meta:
        model = StudentInformation
        fields = '__all__'
        exclude = ()
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "age": forms.NumberInput(attrs={'class': 'form-control'}),
            "sex": forms.Select(attrs={'class': 'select'}),
            "father_name": forms.TextInput(attrs={'class': 'form-control'}),
            "mother_name": forms.TextInput(attrs={'class': 'form-control'}),
            "last_education": forms.TextInput(attrs={'class': 'form-control'}),
        }
