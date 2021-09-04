from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404
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

@login_required
def deleteprofile(request,id):
    context={}
    print(id)
    obj=get_object_or_404(Profile,id=id)
    if request.method=="POST":
        obj.delete()
        return redirect('Landlords')
    return render(request,"landlord/landlordinfo.html",context)
