from django.shortcuts import render,redirect
from .landlord_models import Landlord
#from .form import InsertLandlord
from django.contrib.auth.decorators import login_required
from User.models import Profile


# Create your views here.
@login_required
def Landlordinfo(request) :
    lanlord = Landlord.objects.filter(user=request.user)
    Landlords = Profile.objects.all()
    #print(Landlords)
    if lanlord:
        context = {
            "landlord": True,
            "Landlords" : Landlords
        }
    else:
        context = {
            "Landlords" : Landlords
        }

    return render(request,'landlord/landlordinfo.html',context)




