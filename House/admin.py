from django.contrib import admin
from .house_models import House,Address

# Register your models here.
admin.site.register([House,Address])