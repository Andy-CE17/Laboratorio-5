from django.db import models

class Genre(models.Model): 
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=150, unique=True)
    genres = models.ManyToManyField(Genre, related_name='movies')
    duration = models.PositiveIntegerField(help_text='Duración en minutos')
    synopsis = models.TextField(blank=True)
    release_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self):
        return self.title