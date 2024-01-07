from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('travelspots/', views.travelspots, name='travelspots'),
    path('travelspots/details/<int:id>', views.details, name='details'),
]
