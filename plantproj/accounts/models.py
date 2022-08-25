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
    complexity = models.IntegerField(choices=COMPL)
    lighting = models.CharField(max_length=200, choices=LIGHT)
    waterfreq = models.SmallIntegerField()

    class Meta:
        ordering = ('name',)
        verbose_name = 'Цветок'
        verbose_name_plural = 'Цветы'

    def __str__(self):
        return self.name
