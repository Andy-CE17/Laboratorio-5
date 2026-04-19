from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'genre',
            'duration',
            'synopsis',
            'release_date',
            'is_active',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_duration(self, value):
        if value <= 0:
            raise serializers.ValidationError('La duración debe ser mayor a 0.')
        return value