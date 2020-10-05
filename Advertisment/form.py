from django import forms
from .advertisment_models import Advertisement

class Insertadvertisment(forms.ModelForm):
    class Meta :
        model = Advertisement
        fields = ('landlord', 'house', 'image1', 'image2')