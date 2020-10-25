"""Uroom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import uroomapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', uroomapp.views.main, name='main'),
    path('login/', uroomapp.views.login, name='login'),
    path('manage1/', uroomapp.views.manage1, name='manage1'),
    path('manage2/', uroomapp.views.manage2, name='manage2'),
    path('mypage/', uroomapp.views.mypage, name='mypage'),
    path('newmember/', uroomapp.views.newmember, name='newmember'),
    path('review/', uroomapp.views.review, name='review'),
    path('scrap/', uroomapp.views.scrap, name='scrap'),
    path('seenroom/', uroomapp.views.seenroom, name='seenroom'),
    path('uploadroom/', uroomapp.views.uploadroom, name='uploadroom'),
    path('tradelist/', uroomapp.views.tradelist, name='tradelist'),
    path('reviewlist/', uroomapp.views.reviewlist, name='reviewlist'),
    path('create/', uroomapp.views.create, name='create'),
    path('logout/', uroomapp.views.logout, name='logout'),
]