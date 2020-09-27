"""Home_Rental_Management_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Landlord import views as Lview
from User import views as Uview
from House  import views as Hviews
from Renters import views as Rview
from Advertisment import views as Aview




urlpatterns = [
    path('admin/', admin.site.urls),
    path('Landlords/',Lview.Landlordinfo , name='Landlords'),
    path('Registration/',Uview.registration,name='Registration'),
    path('House/',Hviews.House_info , name='House'),
    path('Renters/',Rview.Rentersinfo),
    path('Advertisment/',Aview.advertisementinfo , name='Advertisment'),
    path('Insertlandlord/',Lview.insertlandlordinfo , name='Insertlandlord'),
    path('accounts/',include('django.contrib.auth.urls'))
    ]

