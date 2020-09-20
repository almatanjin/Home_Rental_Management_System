from django.shortcuts import render
from .models import Advertisement
# Create your views here.
def advertisementinfo(request):
    return render(request,'advertisement/advertisement_info.html')
