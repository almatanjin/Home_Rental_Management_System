from django.shortcuts import render
from .house_models import House
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def House_info(request):
    Houses = House.objects.all()
    print(Houses)
    context = {
        "Houses": Houses
    }
    return render(request,'House/House_info.html',context)