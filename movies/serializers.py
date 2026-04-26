from rest_framework import serializers
from .models import Movie, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)  # ✅ Indentación corregida

    genre_ids = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        many=True,
        write_only=True,
        source='genres'
    )

    class Meta:
        model = Movie
        fields = [
            'id',
            'title',      
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
        if value <= 0:
            raise serializers.ValidationError('La duración debe ser mayor a 0.')
        return value