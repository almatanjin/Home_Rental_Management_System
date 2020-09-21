from django.shortcuts import render
from .advertisment_models import Advertisement
# Create your views here.
def advertisementinfo(request):
    return render(request,'advertisement/advertisement_info.html')
