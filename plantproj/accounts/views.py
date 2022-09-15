from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import Plants,Room
from .filters import OrderFilter

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


# #Figts
# def sportsmen(request):

#     # figters = Fights.objects.using("user").filter
#     figters = Sportsmen.objects.all()
#     myFilter = OrderFilter(request.GET, queryset=figters)
#     figters = myFilter.qs
#     return render(request, 'accounts/sportsBD.html', {'figters': figters, 'myFilter': myFilter})

def plants(request):
    plants = Plants.objects.all()
    myFilter = OrderFilter(request.GET, queryset=plants)
    plants = myFilter.qs
    print(plants)
    return render(request, 'plantsBD.html', {'plants': plants, 'myFilter': myFilter})


def history(request):
    return render(request, 'history.html')
