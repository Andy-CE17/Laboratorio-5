from django.contrib import admin
from .models import Movie, Genre


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'duration',
        'release_date',
        'is_active',
    )  

    search_fields = ('title',) 

    list_filter = ('is_active', 'release_date')  
    filter_horizontal = ('genres',)  

    ordering = ('title',)


@admin.register(Genre)  
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)