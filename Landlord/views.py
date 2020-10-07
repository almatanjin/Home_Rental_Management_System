from django.shortcuts import render,redirect
from .landlord_models import Landlord
#from .form import InsertLandlord
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def Landlordinfo(request) :
    Landlords = Landlord.objects.all()
    print(Landlords)
    context = {
        "Landlords" : Landlords
    }
    return render(request,'landlord/landlordinfo.html',context)
