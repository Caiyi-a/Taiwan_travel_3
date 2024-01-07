from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('write/', views.write, name='write'),
    path('write_result/', views.write_result, name='write_result'),
    path('login_result/', views.login_result, name='login_result'),
    path('article/', views.articles, name='article'),
]