from django.contrib import admin
from .models import Movie, Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    # NUEVO: administración de géneros
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # CAMBIO: administración mejorada de películas
    list_display = (
        'id',
        'title',
        'genre',
        'duration',
        'release_date',
        'is_active',
    )
    search_fields = ('title', 'genre')
    list_filter = ('genre', 'is_active', 'release_date')
    ordering = ('title',)

    # IMPORTANTE: permite seleccionar varios géneros fácilmente
    filter_horizontal = ('genres',)