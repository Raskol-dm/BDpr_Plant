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
