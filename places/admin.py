from django.contrib import admin
from .models import Location, Location_Image


class LocationAdmin(admin.ModelAdmin):
    list_display = ('title',)


class Location_ImageAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Location, LocationAdmin)
admin.site.register(Location_Image, Location_ImageAdmin)
