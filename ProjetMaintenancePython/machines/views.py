from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.


def header(request):
    template = loader.get_template('machines/header.html')
    return HttpResponse(template.render({}, request))


def tableaubord(request):
    essais = Niveau.objects.all()
    template = loader.get_template('machines/interfaceorganisation.html')
    return HttpResponse(template.render({'essais': essais}, request))


def gererEssais(request):
    essais = Essai.objects.all()
    template = loader.get_template('machines/gererEssais.html')
    return HttpResponse(template.render({'essais': essais}, request))


def essai(request):
    essais = Niveau.objects.all()
    modèles = Modele.objects.all()
    template = loader.get_template('machines/essai.html')
    return HttpResponse(template.render({'essais': essais, 'modèles': modèles}, request))
