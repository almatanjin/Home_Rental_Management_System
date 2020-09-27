from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def registration(request) :
    userform = UserCreationForm()
    message = "Welcome"
    if request.method == 'POST' :
        userform = UserCreationForm(request.POST)
        message = "Oops, Try again"
        if userform.is_valid():
            userform.save()
            userform = UserCreationForm()
            message = "Successfull"
            return redirect('login')
    context = {
        "form" : userform,
        "message" : message

    }
    return render(request, 'useregister/useregister.html', context)

