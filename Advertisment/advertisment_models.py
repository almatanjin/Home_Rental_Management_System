from django.db import models
from Landlord .landlord_models import Landlord
from House.house_models import House
# Create your models here.
class Advertisement(models.Model):
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE, default=1)
    house= models.ForeignKey(House,on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='images/Houes', blank=False,default='images/thh.jpg')


    def show(self):
        print("ADVERTISEMENT")
