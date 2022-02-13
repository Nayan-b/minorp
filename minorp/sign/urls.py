from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('showimage/', views.showimage, name='upload'),
    path('verify/', views.verify, name='verify'),
]
