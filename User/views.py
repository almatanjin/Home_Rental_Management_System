from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import  ProfileForm
from .models import Profile
from Landlord.landlord_models import Landlord
from Renters.models import Renter

# Create your views here.

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            st = request.POST.get("landlord")
            if st:
                if int(st)==1:
                    user=form.save()
                    landlord=Landlord(user=user)
                    landlord.save()
                    return redirect('login')
            else:
                user = form.save()
                renter =Renter(user=user)
                renter.save()
                return redirect('login')

    context ={
        'form' : form
    }
    return render(request, 'useregister/useregister.html', context)


@login_required
def create_profile(request):
    form = ProfileForm()

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            profile_object = form.save(commit=False)
            profile_object.user = request.user
            profile_object.save()

            return redirect('view-profile')

    context = {
        'form' : form,
        'landlord':True
    }

    return render(request, 'User/create_profile.html', context)


def view_profile(request):

    profile = Profile.objects.get(user=request.user)
    context = {
        'profile': profile,
        'landlord':True
    }

    return render(request, 'User/view_profile.html', context)

