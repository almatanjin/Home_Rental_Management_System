from django.shortcuts import render,redirect
from .advertisment_models import Advertisement
from .form import Insertadvertisment
from django.contrib.auth.decorators import login_required
from Landlord.landlord_models import Landlord
from django.contrib.auth.models import User
from Renters.models import Renter
# Create your views here.
@login_required
def advertisementinfo(request):
    lanlord =Landlord.objects.filter(user=request.user)
    advertisment = Advertisement.objects.all()
    print(advertisment)

    if request.method == 'POST':
        advertisment = Advertisement.objects.filter(house__address__area__icontains=request.POST['search'])


    if lanlord:
        context = {
        "landlord":True,
        "Advertisment": advertisment
            }
    else:
        context = {
          "Advertisment": advertisment
        }
    return render(request,'advertisement/advertisement_info.html',context)





@login_required
def insertadvertismentinfo(request):
    form = Insertadvertisment()
    landlord = Landlord.objects.get(user=request.user)

    #if landlord:
    message = "Insert Advertisement Information"
    if request.method == 'POST':
        form = Insertadvertisment(request.POST, request.FILES)
        message = "Oops,Try again"
        if form.is_valid():
            ads = form.save(commit=False)
            ads.landlord = landlord
            ads.save()
            form = Insertadvertisment()
            message = "Successfull !"
            return redirect('Advertisment')

    context = {
            'form': form,
            'message': message,
            'landlord': True
        }
    return render(request, 'advertisement/insertadvertisment.html', context)
    #else:
        #return render(request, 'advertisement/advertisement_info.html', context)
        #redirect("Advertisment")

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
