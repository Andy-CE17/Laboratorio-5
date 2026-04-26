from rest_framework import serializers, viewsets
from .models import Ticket
from .serializers import TicketSerializer


class TicketViewSet(viewsets.ModelViewSet):
    # NUEVO: CRUD completo para tickets
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def perform_create(self, serializer):
        # IMPORTANTE: obtener la función seleccionada
        showtime = serializer.validated_data['showtime']

        # IMPORTANTE: asientos que el cliente quiere reservar
        seats_requested = serializer.validated_data['seats']

        # IMPORTANTE: capacidad total de la sala
        room_capacity = showtime.room.capacity

        # IMPORTANTE: sumar asientos ya reservados para esa función
        tickets_sold = sum(
            ticket.seats for ticket in showtime.tickets.all()
        )

        # VALIDACIÓN: no vender más asientos que la capacidad
        if tickets_sold + seats_requested > room_capacity:
            raise serializers.ValidationError(
                'No hay suficientes asientos disponibles para esta función.'
            )

        serializer.save()