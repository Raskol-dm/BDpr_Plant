from pyexpat import model
from django.db import models

# Наша база данных
# Create your models here.


class Plants(models.Model):
    COMPL = (
        ('Master', 'master'),
        ('Middle', 'middle'),
        ('Beginner', 'beginner'),
    )
    LIGHT = (
        ('Sunny', 'sunny'),
        ('Half-shade', 'half-shade'),
        ('Dark', 'dark'),

    )
    name = models.CharField(max_length=200)
    kind = models.CharField(max_length=200)
    height = models.SmallIntegerField()
    complexity = models.CharField(max_length=20,choices=COMPL)
    lighting = models.CharField(max_length=20, choices=LIGHT)
    waterfreq = models.SmallIntegerField()
    # nextFreq = models.DateField() - для одного

    class Meta:
        ordering = ('name',)
        verbose_name = 'Цветок'
        verbose_name_plural = 'Цветы'

    def __str__(self):
        return self.name


class Room(models.Model):
    rname = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    plrelation = models.ManyToManyField(Plants)
    # created = models.DateField(auto_now_add=True)
    # upwaterfreq = models.DateField(auto_now=True)

    class Meta:
        ordering = ('user_id',)
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

    def __str__(self):
        return self.rname


# class Room(models.Model):
#     user = models.ForeignKey(
#         to=User, on_delete=models.CASCADE, related_name='owner')
#     plants = models.ManyToManyField(Plant, related_name='plants_rooms')

class Watrlogs(models.Model):
    room_id = models.ForeignKey('Room', on_delete=models.CASCADE)
    pname_id = models.ForeignKey('Plants', on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    upwaterfreq = models.DateField(auto_now=True)
    nextwaterfreq = models.DateField(auto_now=True)

    class Meta:
        ordering = ('room_id',)
        verbose_name = 'Журнал полива'
        verbose_name_plural = 'Журнал поливов'


