from django import forms
from .models import Renter

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Renter
        fields = ('contact_no','name','email')