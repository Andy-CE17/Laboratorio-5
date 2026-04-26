from rest_framework import serializers
from .models import Movie, Genre


class GenreSerializer(serializers.ModelSerializer):
    # NUEVO: serializer para Genre
    class Meta:
        model = Genre
        fields = ['id', 'name']


class MovieSerializer(serializers.ModelSerializer):
    # CAMBIO: muestra los géneros completos al consultar películas
    genres = GenreSerializer(many=True, read_only=True)

    # NUEVO: permite enviar IDs de géneros al crear/editar películas
    genre_ids = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        many=True,
        write_only=True,
        source='genres',
        required=False
    )

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
            'genres',
            'genre_ids',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_duration(self, value):
        # VALIDACIÓN: la duración debe ser mayor a 0
        if value <= 0:
            raise serializers.ValidationError('La duración debe ser mayor a 0.')
        return value