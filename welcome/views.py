import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from .models import Task

from . import database
from .models import PageView

# Create your views here.

def index(request):
    """Takes an request object as a parameter and creates an pageview object then responds by rendering the index view."""
    tasks = Task.objects.all()
    return render(request, 'welcome/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})

def health(request):
    """Takes an request as a parameter and gives the count of pageview objects as reponse"""
    return render(request, 'welcome/about.html')
