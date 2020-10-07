from django.shortcuts import render,redirect
from .house_models import House
from .form import InsertHouse,InsertAddress
from django.contrib.auth.decorators import login_required
from Landlord.landlord_models import Landlord
from django.contrib.auth.models import User


# Create your views here.
@login_required
def House_info(request):
    Houses = House.objects.all()

    print(Houses)


    #if request.method == 'POST':

        #Houses = House.objects.filter(address__area__icontains=request.POST['search'])




    context = {
        "Houses": Houses,
        #"Addresses" : Addresses
    }
    return render(request,'House/House_info.html',context)


@login_required
def insertHouseinfo(request):
    form = InsertHouse()
    landlord = Landlord.objects.get(user= request.user)
    #if landlord:
    message = "Insert House Information"
    if request.method == 'POST':
        form = InsertHouse(request.POST, request.FILES)
        message = "Oops,Try again"

        if form.is_valid():
            house = form.save(commit=False)
            # house.user =request.user
            house.landlord = landlord
            house.save()
            form = InsertHouse()
            message = "Successfull !"
            return redirect('House')

    context = {
            'form': form,
            'message': message,

        }
    return render(request, 'House/inserthouse.html', context)
    #else:
        #return render(request, 'House/advertisement_info.html', context)
        #redirect ("Advertisment")

@login_required
def insertaddressinfo(request):
    form = InsertAddress()
    message="Insert house address"
    if request.method == 'POST' :
        form = InsertAddress(request.POST)
        message = "Oops,Try again"
        if form.is_valid():
            form.save()
            form = InsertAddress()
            message = "Successful!!"
            return redirect('InsertHouse')
    context = {
        'form' : form,
        'message' : message
    }
    return render(request,'house/insertaddress.html',context)