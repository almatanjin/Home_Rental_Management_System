from django.shortcuts import render
from .models import Landlord


# Create your views here.
def Landlordinfo(request) :
    Landlords = Landlord.objects.all()
    print(Landlords)
    context = {
        "Landlords" : Landlords
    }
    return render(request,'landlord/landlordinfo.html',context)