from django.contrib import admin
from . models import House,Address

# Register your models here.
admin.site.register([House,Address])