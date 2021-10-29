from django.contrib.auth import forms
from django.http import response
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    form = UserCreationForm() # creating instance
    return render(request, 'users/register.html', {'form' : form})
    