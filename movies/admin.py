from django.contrib import admin
from .models import Movie, Genre 

@admin.register(Genre)  # NUEVO
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
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
    filter_horizontal = ('genres',)  # NUEVO (mejor UX para ManyToMany)