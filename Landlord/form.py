from django import forms
from .models import Landlord

class InsertLandlord(forms.ModelForm):
    class Meta :
        model = Landlord
        fields =('name','Contact_number','email')