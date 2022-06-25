from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('details', views.details, name='details'),
    path('Listing', views.Listing, name='Listing'),
    path('sarchform', views.sarchform, name='sarchform'),
    path('index', views.index, name='index'),
]