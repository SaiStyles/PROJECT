"""
URL configuration for crime project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from cApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('userReg', views.userReg),
    path('login/', views.login),

    path('adminHome', views.adminHome),
    path('adminUsers', views.adminUsers),
    path('adminUpdateUsers', views.adminUpdateUsers),
    path('adminAnalysis', views.adminAnalysis),
    path('adminAnalysisState', views.adminAnalysisState),
    path('adminPrediction', views.adminPrediction),
    path('adminchats', views.adminchats),
    path('adminChat', views.adminChat),
    path('adminCrime', views.adminCrime),


    path('userHome', views.userHome),
    path('userAnalysis', views.userAnalysis),
    path('userPrediction', views.userPrediction),
    path('useradminchat', views.useradminchat),
    path('UserIndiaAnalysis', views.UserIndiaAnalysis),
    path('userAddCrime', views.userAddCrime),
    path('userViewCrime', views.userViewCrime),
    path('userUpdateCrimeFile', views.userUpdateCrimeFile),
    path('udp', views.udp),



]
