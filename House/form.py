from django import forms
from .house_models import House


class InsertHouse(forms.ModelForm):
    class Meta:
        model = House
        fields = ('size_in_sqfeet', 'rent', 'room_no', 'address','landlord','image')
