from django.db import models


# Create your models here.
class House(models.Model):
    room_no =  models.IntegerField(max_length=10)
    size_in_sqfeet = models.IntegerField(max_length=10)
    rent = models.IntegerField(max_length=25)
