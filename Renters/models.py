from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Renter(models.Model):

    #profile_picture = models.ImageField(upload_to='images/profile', blank=True, default='images/thh.jpg')
    contact_no = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=100, null=True, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=1)
    def __str__(self):
        return self.user.username
