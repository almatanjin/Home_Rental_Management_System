from django.db import models

# Create your models here.
class Advertisement(models.Model):
    def show(self):
        print("ADVERTISEMENT")