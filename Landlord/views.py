from django.shortcuts import render
from .landlord_models import Landlord
from .form import InsertLandlord
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
@login_required
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