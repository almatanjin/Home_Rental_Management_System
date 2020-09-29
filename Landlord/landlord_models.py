from django.db import models


# Create your models here.
class Landlord(models.Model):
    name = models.CharField(max_length=100)
    Contact_number = models.IntegerField()
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name
