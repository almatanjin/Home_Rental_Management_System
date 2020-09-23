from django.shortcuts import render
from .models import Renters


# Create your views here.
def Rentersinfo(request) :
    renters = Renters.objects.all()
    print(renters)
    context = {
        "Renters" : renters
    }
    return render(request,'renters/renterinfo.html',context)