from django.shortcuts import render,redirect
from .models import Renter
from django.contrib.auth.decorators import login_required
from .form import ProfileForm
from Landlord.landlord_models import Landlord

# Create your views here.
def Rentersinfo(request) :
    renters = Renter.objects.all()
    print(renters)
    context = {
        "Renters" : renters
    }
    return render(request,'renters/renterinfo.html',context)

