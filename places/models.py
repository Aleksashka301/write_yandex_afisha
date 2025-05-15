from django.db import models
from django.utils.html import mark_safe
from tinymce.models import HTMLField


class Location(models.Model):
    title = models.CharField(verbose_name='Название локации', max_length=100)
    description_short = models.TextField(verbose_name='Краткое описание')
    description_long = HTMLField(verbose_name='Описание')
    coordinates_lng = models.DecimalField(verbose_name='Координаты долготы', max_digits=20, decimal_places=15)
    coordinates_lat = models.DecimalField(verbose_name='Координаты широты', max_digits=20, decimal_places=15)

    class Meta:
        ordering = ['id']


class LocationImage(models.Model):
    title = models.CharField(verbose_name='Название картинки', max_length=100)
    image = models.ImageField(verbose_name='Картинка')
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='images',
        null=True,
        verbose_name='Локация',
    )

    def image_preview(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" style="max-height: 200px;" />')
        return "Нет изображения"

    class Meta:
        ordering = ['order']

