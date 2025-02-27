import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

from . import database
from .models import PageView

# Create your views here.

def index(request):
    """Takes an request object as a parameter and creates an pageview object then responds by rendering the index view."""
    tasks = Task.objects.all()
    return render(request, 'welcome/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})

def health(request):
    """Takes an request as a parameter and gives the count of pageview objects as reponse"""
    return HttpResponse(PageView.objects.count())

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Ошибка в форме'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'welcome/about.html', context)
