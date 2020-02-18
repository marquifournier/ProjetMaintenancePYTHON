from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def header(request):
    template = loader.get_template('machines/header.html')
    return HttpResponse(template.render({}, request))

def tableaubord(request):
    template = loader.get_template('machines/tableaubord.html')
    return HttpResponse(template.render({}, request))