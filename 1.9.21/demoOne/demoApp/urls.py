from django import urls
from django.urls import path
from django.urls.conf import include
from . import views #from all import views

urlpatterns = [
    path('', views.home, name='home'),  # home page urls
    path('add', views.add, name='add'),
    
]
