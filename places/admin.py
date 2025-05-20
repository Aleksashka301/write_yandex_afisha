from adminsortable2.admin import SortableTabularInline, SortableAdminMixin
from django.contrib import admin

from .models import Location, LocationImage


class LocationImageInline(SortableTabularInline):
    model = LocationImage
    readonly_fields = ('image_preview',)
    fields = ('image', 'image_preview',)


@admin.register(Location)
class LocationAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title',)
    inlines = [LocationImageInline,]


@admin.register(LocationImage)
class LocationImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'location',)
    raw_id_fields = ('location', )
