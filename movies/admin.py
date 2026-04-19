from django.contrib import admin
from .models import Movie


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