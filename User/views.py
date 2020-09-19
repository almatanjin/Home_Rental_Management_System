from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def registration(request) :
    userform = UserCreationForm()
    if request.method == 'POST' :
        userform = UserCreationForm(request.POST)
        if userform.is_valid():
            userform.save()

    context = {
        "form" : userform

    }
    return render(request,'register/useregister.html',context)

