from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('header', views.header, name='header'),
    path('', views.tableaubord, name='tableaubord')
]