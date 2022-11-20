from operator import imod
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User

class RoomForm(ModelForm):
	class Meta:
		model = Room
		fields = 'rname', 'is_active'


class PlantForm(ModelForm):
	class Meta:
		model = Room
		fields = 'rname','is_active', 'plrelation'


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
