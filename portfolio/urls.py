from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('sarbesh', views.sarbesh, name='sarbesh'),
    path('', views.index, name='index'),
    path('<slug:slug>',views.my, name='my'),
]
