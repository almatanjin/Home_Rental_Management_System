from django.shortcuts import render
from .house_models import House

# Create your views here.
def House_info(request):
    Houses = House.objects.all()
    print(Houses)
    context = {
        "Houses": Houses
    }
    return render(request,'House/House_info.html',context)