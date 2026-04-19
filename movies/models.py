from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=150)
    genre = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(help_text="Duración en minutos")
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self):
        return self.title