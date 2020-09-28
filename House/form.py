from django import forms
from .house_models import House

class InsertHouse(forms.ModelForm):
    class Meta :
        model = House
        fields ='__all__'