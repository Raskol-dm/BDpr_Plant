from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.models import Plants, Room, Watrlogs
from .filters import OrderFilter
from datetime import date
from .forms import *
from django.db.models import F
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import connections

from django.contrib import messages

# Функции и классы, активирующие наши шаблоны URL
# Create your views here.


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # user = form.save()
            # print("Firs: ", user)
            # group = Group.objects.get(name='user')
            # print(group)
            # user.groups.add(group)
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def loginPage(request):
    print("СВЯЗЬ!")
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # print(user)
                # if user == 'dima':
                #     conn = connections['default']
                #     conn.connect()
                # else:
                #     print(user)
                #     group = user.groups.all()[0].name
                #     print(user)
                #     print(group)
                #     conn = connections[group]
                #     print(conn)
                #     conn.connect()
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
def home(request):
    rmk = []
    roomPlants = []
    rooms = Room.objects.filter(
        user_id=request.user.id).prefetch_related('plrelation')
    for rome in rooms:
        roomPlants.append(rome.plrelation.all())
        rmk.append(rome.id)

    total_plants = Room.objects.filter(
        user_id=request.user.id).prefetch_related('plrelation').count()
    print('Всего ратс', total_plants)
    water_need = Watrlogs.objects.filter(
        nextwaterfreq__lte=date.today()).count()
    print('Требуется полить', water_need)
    print(roomPlants)
    print('Set', rmk)
    dtlogs = Watrlogs.objects.filter(room_id__in=rmk)
    print(dtlogs)
    return render(request, 'dashboard.html', {'rooms': rooms, 'roomPlants': roomPlants, 'dtlogs': dtlogs, 'total_plants': total_plants, 'water_need': water_need})


@login_required(login_url='login')
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
@login_required(login_url='login')
def plants(request):
    plants = Plants.objects.all()
    myFilter = OrderFilter(request.GET, queryset=plants)
    plants = myFilter.qs
    print(plants)
    return render(request, 'plantsBD.html', {'plants': plants, 'myFilter': myFilter})


@login_required(login_url='login')
def history(request):
    return render(request, 'history.html')


def roomAdd(request):

    form = RoomForm()

    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user_id = request.user
            obj.save()
            return redirect('/')

    context = {'form':form}

    
    return render(request, 'room_form.html', context)


def plantAdd(request):

    form = PlantForm()

    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = PlantForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user_id = request.user
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'plant_form.html', context)


def deleteRoom(request):
	rmdel = Room.objects.get()
	if request.method == "POST":
		rmdel.delete()
		return redirect('/')

	context = {'item': rmdel}
	return render(request, 'accounts/delete.html', context)

# def waterfr(request):

#     watfr = Watrlogs.objects.update(upwaterfreq = date.today())
#     watfr.save()


# def updateMathes(request, pk):
# 	form = FightForm()
# 	fights = Room.objects.get(id=pk)
# 	form = RoomForm(instance=fights)

# 	if request.method == 'POST':
# 		form = RoomForm(request.POST, instance=fights)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('/')

# 	context = {'form': form}
# 	return render(request, 'accounts/rom_form.html', context)
