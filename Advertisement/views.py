from django.shortcuts import render
from .advertisment_models import Advertisement
# Create your views here.
def advertisementinfo(request):
    advertisment = Advertisement.objects.all()
    print(advertisment)
    context = {
        "Advertisment": advertisment
    }
    return render(request,'advertisement/advertisement_info.html',context)
