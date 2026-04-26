from django.contrib import admin
<<<<<<< HEAD
from .models import Movie, Genre
=======
from .models import Movie, Genre 
>>>>>>> f017fb2bdc19ce0f06413ed1af12417451952a53

@admin.register(Genre)  # NUEVO
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'duration',
        'release_date',
        'is_active',
<<<<<<< HEAD
    )  

    search_fields = ('title',) 

    list_filter = ('is_active', 'release_date')  
    filter_horizontal = ('genres',)  

    ordering = ('title',)


@admin.register(Genre)  
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
=======
    )
    search_fields = ('title', 'genre')
    list_filter = ('genre', 'is_active', 'release_date')
    ordering = ('title',)
    filter_horizontal = ('genres',)  # NUEVO (mejor UX para ManyToMany)
>>>>>>> f017fb2bdc19ce0f06413ed1af12417451952a53
