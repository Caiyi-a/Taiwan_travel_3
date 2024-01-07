from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect
from django.template import loader
from .models import Activity

# Create your views here.
def activities(request):
  activities = Activity.objects.all()
  template = loader.get_template('all_activities.html')
  context = {
    'activities': activities,
  }
  return HttpResponse(template.render(context, request))