from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Renters(models.Model):
    #name = models.CharField(max_length=100)
    #Contact_number = models.IntegerField()
    #email = models.EmailField(max_length=100)
    #area = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=1)

    def __str__(self):
        return self.user.username
