from django.urls import path
from django.views import View
from . import views

urlpatterns = [
    path('database/', views.plants),
    path('', views.home,name="home"),
    path('room/', views.room),
    path('history/', views.history),
    path('room_add', views.roomAdd, name="room_add"),
    path('plant_add', views.plantAdd, name="plant_add"),
    path('delete_room', views.deleteRoom, name="delete_room"),
    path('register/', views.registerPage, name="register"),
   	path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout")

]
