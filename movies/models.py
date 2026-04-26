from django.db import models


class Genre(models.Model):
    # NUEVO: entidad Genre
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return self.name


class Movie(models.Model):
    # MODELO PRINCIPAL DE PELÍCULAS
    title = models.CharField(max_length=150, unique=True)
    genre = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(help_text='Duración en minutos')
    synopsis = models.TextField(blank=True)
    release_date = models.DateField()
    is_active = models.BooleanField(default=True)

    # NUEVO: relación muchos a muchos con Genre
    genres = models.ManyToManyField(
        Genre,
        related_name='movies',
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self):
        return self.title