from django.db import models
from movies.models import Movie  # IMPORTANTE


class Room(models.Model):
    # NUEVO: Sala de cine
    name = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Showtime(models.Model):
    # NUEVO: Función de película
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='showtimes'
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name='showtimes'
    )
    date_time = models.DateTimeField()

    def __str__(self):
        return f"{self.movie.title} - {self.date_time}"