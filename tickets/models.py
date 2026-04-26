from django.db import models
from showtimes.models import Showtime


class Ticket(models.Model):
    # NUEVO: relación con la función de cine
    showtime = models.ForeignKey(
        Showtime,
        on_delete=models.CASCADE,
        related_name='tickets'
    )

    # NUEVO: datos del cliente
    customer_name = models.CharField(max_length=100)

    # NUEVO: cantidad de asientos reservados
    seats = models.PositiveIntegerField()

    # NUEVO: fecha de creación automática
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'

    def __str__(self):
        return f'{self.customer_name} - {self.seats} asiento(s)'