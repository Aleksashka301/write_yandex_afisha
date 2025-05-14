from django.contrib import admin
from .models import Location, Location_Image


class Location_ImageInline(admin.TabularInline):
    model = Location_Image


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [Location_ImageInline,]


@admin.register(Location_Image)
class Location_ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'location',)
