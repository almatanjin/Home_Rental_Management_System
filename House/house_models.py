from django.db import models
from Landlord.landlord_models import Landlord
from django.contrib.auth.models import User


# Create your models here.
class Address(models.Model):
    city = models.CharField(max_length=25)
    house_no = models.IntegerField(max_length=10)
    road_no = models.IntegerField(max_length=10)
    area = models.CharField(max_length=25)

    def __str__(self):
        return str(self.road_no) + " " + self.area + " ," + self.city


class House(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE, default=1)
    size_in_sqfeet = models.IntegerField(max_length=10)
    rent = models.IntegerField(max_length=25)
    room_no = models.IntegerField(max_length=10)

    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE, default=1) #User
    image = models.ImageField(upload_to='images/Houes', blank=True, default='images/thh.jpg')


    #def __str__(self):
       # return self.address.city
