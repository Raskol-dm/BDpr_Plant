from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import Plants,Room

# Функции и классы, активирующие наши шаблоны URL
# Create your views here.


def home(request):
    roomPlants = []
    rooms = Room.objects.filter(user_id = request.user.id).prefetch_related('plrelation')
    for rome in rooms:
        roomPlants.append(rome.plrelation.all())
    print(roomPlants)
    return render(request, 'dashboard.html', {'rooms': rooms, 'roomPlants': roomPlants})


def room(request):
    return render(request, 'room.html')


def plants(request):
    return render(request, 'plantsBD.html')


def history(request):
    return render(request, 'history.html')
