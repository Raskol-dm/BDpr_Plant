from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import Plants,Room, Watrlogs
from .filters import OrderFilter
from datetime import date

# Функции и классы, активирующие наши шаблоны URL
# Create your views here.


def home(request):
    rmk = []
    roomPlants = []
    rooms = Room.objects.filter(user_id = request.user.id).prefetch_related('plrelation')
    for rome in rooms:
        roomPlants.append(rome.plrelation.all())
        rmk.append(rome.id)

    total_plants = Room.objects.filter(
        user_id=request.user.id).prefetch_related('plrelation').count()
    print('Всего ратс', total_plants)
    water_need = Watrlogs.objects.filter(nextwaterfreq__lte=date.today()).count()
    print('Требуется полить', water_need)
    print(roomPlants)
    print('Set', rmk)
    dtlogs = Watrlogs.objects.filter(room_id__in=rmk)
    print(dtlogs)
    return render(request, 'dashboard.html', {'rooms': rooms, 'roomPlants': roomPlants, 'dtlogs': dtlogs, 'total_plants': total_plants, 'water_need': water_need})


def room(request):
    rooms = Room.objects.filter(user_id=request.user.id)
    return render(request, 'room.html', {'rooms': rooms})


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
