from django.shortcuts import render
from .models import Landlord
from .form import InsertLandlord


# Create your views here.
def Landlordinfo(request) :
    Landlords = Landlord.objects.all()
    print(Landlords)
    context = {
        "Landlords" : Landlords
    }
    return render(request,'landlord/landlordinfo.html',context)

def insertlandlordinfo(request):
    form = InsertLandlord()
    message="Insert Landlord Information"
    if request.method == 'POST' :
        form = InsertLandlord(request.POST)
        message = "Oops,Try again"
        if form.is_valid():
            form.save()
            form = InsertLandlord()
            message = "Successfully you become a landord.Now you an letout you house for rent."

    context = {
        'form' : form,
        'message' : message
    }
    return render(request,'landlord/insertlandlord.html',context)