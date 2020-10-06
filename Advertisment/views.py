from django.shortcuts import render,redirect
from .advertisment_models import Advertisement
from .form import Insertadvertisment
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def advertisementinfo(request):
    advertisment = Advertisement.objects.all()
    print(advertisment)

    if request.method == 'POST':
        advertisment = Advertisement.objects.filter(house__address__area__icontains=request.POST['search'])
        #addresses = Address.objects.filter(area__icontains=request.POST['search'])


    context = {
        "Advertisment": advertisment
    }
    return render(request,'advertisement/advertisement_info.html',context)





@login_required
def insertadvertismentinfo(request):
    form = Insertadvertisment()
    message="Insert Advertisement Information"
    if request.method == 'POST' :
        form = Insertadvertisment(request.POST, request.FILES)
        message = "Oops,Try again"
        if form.is_valid():
            form.save()
            form = Insertadvertisment()
            message = "Successfull !"
            return redirect('Advertisment')

    context = {
        'form' : form,
        'message' : message
    }
    return render(request,'advertisement/insertadvertisment.html',context)

def advertisementpic(request):
    advertisment = Advertisement.objects.all()
    print(advertisment)

    context = {
        "Advertisment": advertisment,

    }
    return render(request,'advertisement/home.html',context)






@login_required
def showAdvertisement(request, advertisement_id):

    searched_Advertisment=  Advertisement.objects.filter( id=advertisement_id)
    print(searched_Advertisment)



    if len (searched_Advertisment)==0:
        does_exists =False
        context = {
            'does_exists': does_exists,
        }
    else:
        does_exists = True
        search = searched_Advertisment[0]
        context = {
        'does_exists': does_exists,
        'search': search
       }

    return render(request, 'advertisement/advertisement_detailsview.html', context)
