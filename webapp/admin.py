from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('fan_start', 'fan_stop', 'start_at', 'end_at')
@admin.register(models.Greenhouse)
class GreenhouseAdmin(admin.ModelAdmin):
    list_display = ('temp', 'humid', 'moist')

