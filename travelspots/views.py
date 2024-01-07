from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Travelspot, City, Hot

# Create your views here.
def travelspots(request):
    mytravelspots = Travelspot.objects.all().values()
    template = loader.get_template('all_travelspots.html')
    context = {
        'mytravelspots': mytravelspots,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mycity = City.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mycity': mycity,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    myhot = Hot.objects.all()
    template = loader.get_template('main.html')
    context = {
        'myhot': myhot,
    }
    return HttpResponse(template.render(context, request))

def master(request):
    mytravelspots = Travelspot.objects.all()
    template = loader.get_template('master.html')
    context = {
        'mytravelspots': mytravelspots,
    }
    return HttpResponse(template.render(context, request))