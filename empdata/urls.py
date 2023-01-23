"""empdata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from empapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get',views.gettingdata),
    path('show',views.show,name="show"),
    path('Hyderabad',views.Hyderabad,name="Hyderabad"),
    path('Bang',views.Banglore,name="Bang"),
    path('Chennai',views.Chennai,name="Chennai"),
    path('Pune',views.Pune,name="Pune"),
    path('',views.show),
    path('Home',views.Homepage,name="Home")
    
]
