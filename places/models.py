from django.db import models


class Location(models.Model):
    title = models.CharField(verbose_name='Название локации', max_length=100)
    description_short = models.TextField(verbose_name='Краткое описание')
    description_long = models.TextField(verbose_name='Описание')
    coordinates_lng = models.DecimalField(verbose_name='Координаты долготы', max_digits=20, decimal_places=15)
    coordinates_lat = models.DecimalField(verbose_name='Координаты широты', max_digits=20, decimal_places=15)


class Location_Image(models.Model):
    title = models.CharField(verbose_name='Название картинки', max_length=100)
    image = models.ImageField(verbose_name='Картинка')
