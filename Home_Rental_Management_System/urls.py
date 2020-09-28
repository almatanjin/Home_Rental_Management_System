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
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('Landlords/',Lview.Landlordinfo , name='Landlords'),
    path('Registration/',Uview.register,name='Registration'),
    path('House/',Hviews.House_info , name='House'),
    path('Renters/',Rview.Rentersinfo),
    path('Advertisment/',Aview.advertisementinfo , name='Advertisment'),
    path('Insertlandlord/',Lview.insertlandlordinfo , name='Insertlandlord'),
<<<<<<< HEAD
    path('accounts/',include('django.contrib.auth.urls')),
    path('create-profile/', Uview.create_profile, name='create-profile'),
    path('view-profile/', Uview.view_profile, name='view-profile'),
]
=======
    path('InsertHouse/', Hviews.insertHouseinfo, name='InsertHouse'),
    path('accounts/',include('django.contrib.auth.urls'))
    ]
>>>>>>> a459aedb0f266c4f6dc55ef89008ba5467df7060


if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)