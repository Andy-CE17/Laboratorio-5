from rest_framework import serializers
from .models import Movie, Genre


class GenreSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)  

    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'genres',
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