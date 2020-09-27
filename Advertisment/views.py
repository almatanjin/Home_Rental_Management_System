from django.shortcuts import render
from .advertisment_models import Advertisement
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def advertisementinfo(request):
    advertisment = Advertisement.objects.all()
    print(advertisment)
    context = {
        "Advertisment": advertisment
    }
    return render(request,'advertisement/advertisement_info.html',context)