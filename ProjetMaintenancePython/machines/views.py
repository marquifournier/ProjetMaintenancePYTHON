from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def header(request):
    template = loader.get_template('machines/header.html')
    return HttpResponse(template.render({}, request))

def tableaubord(request):
    template = loader.get_template('machines/interfaceorganisation.html')
    return HttpResponse(template.render({}, request))

def gererEssais(request):
    template = loader.get_template('machines/gererEssais.html')
    return HttpResponse(template.render({}, request))

def essai(request):
    template = loader.get_template('machines/essai.html')
    return HttpResponse(template.render({}, request))
