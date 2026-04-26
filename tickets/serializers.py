from rest_framework import serializers
from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            'id',
            'showtime',
            'customer_name',
            'seats',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']

    def validate_seats(self, value):
        # VALIDACIÓN: no permitir 0 asientos
        if value <= 0:
            raise serializers.ValidationError(
                'La cantidad de asientos debe ser mayor a 0.'
            )
        return value