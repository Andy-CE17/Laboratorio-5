from django.contrib import admin
from .models import Room, Showtime


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'capacity')


@admin.register(Showtime)
class ShowtimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'room', 'date_time')