from django.urls import path
from django.views import View
from . import views

urlpatterns = [
    path('database/', views.plants),
    path('', views.home),
    path('room/', views.room),
    path('history/', views.history)

]
