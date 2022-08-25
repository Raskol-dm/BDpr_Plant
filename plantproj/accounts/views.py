from django.shortcuts import render
from django.http import HttpResponse


# Функции и классы, активирующие наши шаблоны URL
# Create your views here.

def home(request):
    return render(request, 'dashboard.html')


def room(request):
    return render(request, 'room.html')


def plants(request):
    return render(request, 'plantsBD.html')


def history(request):
    return render(request, 'history.html')
