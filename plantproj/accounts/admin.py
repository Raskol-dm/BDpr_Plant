from django.contrib import admin

from .models import *

# Администрирование
# Register your models here.


@admin.register(Plants)
class PlantsAdmin(admin.ModelAdmin):
    list_display = ['name', 'kind', 'height',
                    'complexity', 'lighting', 'waterfreq']
