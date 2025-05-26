from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField


class Location(models.Model):
    title = models.CharField(verbose_name='Название локации', max_length=100, unique=True)
    short_description = models.TextField(verbose_name='Краткое описание', blank=True)
    long_description = HTMLField(verbose_name='Описание', blank=True)
    lng_coordinates = models.DecimalField(verbose_name='Координаты долготы', max_digits=20, decimal_places=15)
    lat_coordinates = models.DecimalField(verbose_name='Координаты широты', max_digits=20, decimal_places=15)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title


class LocationImage(models.Model):
    image = models.ImageField(verbose_name='Картинка')
    order = models.PositiveIntegerField(
      verbose_name='Поле для сортировки',
      default=0,
      blank=False,
      null=False,
      db_index=True
    )

    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Локация',
    )

    class Meta:
        ordering = ['order']

    def image_preview(self):
        if self.image:
            return format_html(
                '<img src="{}" style="max-width: 300px; max-height: 300px;" />',
                self.image.url
            )
        return "Нет изображения"
