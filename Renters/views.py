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

@login_required
def renterprofile(request):
    form = ProfileForm()

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            profile_object = form.save(commit=False)
            profile_object.user = request.user
            profile_object.save()

            return redirect('rview-profile')

    context = {
        'form' : form,
        'landlord':False
    }

    return render(request, 'renters/create_profile.html', context)

@login_required
def rviewprofile(request):
    lanlord = Landlord.objects.filter(user=request.user)

    profile = Renter.objects.filter(user=request.user)

    if lanlord:
        context = {
            'profile': profile,
            "landlord": True
        }
    else:
        context = {
            'profile': profile,
            "landlord":False

        }

    return render(request, 'renters/view_profile.html', context)