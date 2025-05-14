from django.contrib import admin
from .models import Location, Location_Image


class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)


class Location_ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'location',)


admin.site.register(Location, LocationAdmin)
admin.site.register(Location_Image, Location_ImageAdmin)
