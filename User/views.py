from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import  ProfileForm
from .models import Profile

# Create your views here.

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
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

            return redirect('Advertisment')

    context = {
        'form' : form
    }

    return render(request, 'User/create_profile.html', context)


def view_profile(request):
    profile = Profile.objects.get(user=request.user)
    context = {
        'profile': profile
    }

    return render(request, 'User/view_profile.html', context)

