from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Landlord(models.Model):
    #name = models.CharField(max_length=100)
    #Contact_number = models.IntegerField(null=True,default=1)
    #email = models.EmailField(max_length=100,null=True,default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, default=1)



    def __str__(self):
        return self.user.username
