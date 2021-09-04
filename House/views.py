from django.shortcuts import render,redirect,get_object_or_404
from .house_models import House
from .form import InsertHouse,InsertAddress
from django.contrib.auth.decorators import login_required
from Landlord.landlord_models import Landlord
from django.contrib.auth.models import User


# Create your views here.
@login_required
def House_info(request):
    lanlord = Landlord.objects.filter(user=request.user)
    Houses = House.objects.all()

    print(Houses)


    #if request.method == 'POST':

        #Houses = House.objects.filter(address__area__icontains=request.POST['search'])
    if lanlord:
        context = {
            "landlord": True,
            "Houses": Houses,
        }
    else:
        context = {
            "Houses": Houses,
        }





    return render(request,'House/House_info.html',context)


@login_required
def insertHouseinfo(request):
    form = InsertHouse()
    landlord = Landlord.objects.get(user= request.user)
    if Landlord:
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
            'landlord':True

        }
        return render(request, 'House/inserthouse.html', context)

    else:
        return render(request, 'House/advertisement_info.html')
        #redirect ("Advertisment")

@login_required
def insertaddressinfo(request):
    form = InsertAddress()
    landlord = Landlord.objects.get(user=request.user)
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
        'message' : message,
        'landlord':True
    }
    return render(request,'house/insertaddress.html',context)
@login_required
def showhouse(request, house_id):

    searched_Advertisment=  House.objects.filter( id=house_id)
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

    return render(request, 'House/House_info.html', context)

@login_required

def delete_house(request, id):
    context={}
    print(id)
    pi = get_object_or_404(House, id=id)


    pi.delete()
    return redirect('House')

    return render(request,'House/House_info.html',context)
# @login_required
# def update_data(request,id):
#     if request=="post":
#         pi=House.objects.get(pk=id)
#         fm=InsertHouse(request.POST,instance=pi)
#         if fm.is_valid():
#             fm.save()