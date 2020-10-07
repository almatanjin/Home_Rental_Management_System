from django import forms
from .house_models import House,Address


class InsertHouse(forms.ModelForm):
    class Meta:
        model = House
        fields = ( 'address','size_in_sqfeet', 'rent', 'room_no','image')
class InsertAddress(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('city','house_no','road_no','area')
