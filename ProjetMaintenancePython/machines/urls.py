from django.urls import path
from . import views

urlpatterns = [
    path('header', views.header, name='header'),
    path('', views.tableaubord, name='interfaceOrganisation'),
    path('gererEssais', views.gererEssais, name="gererEssais"),
    path('essai', views.essai, name="essai")
]
