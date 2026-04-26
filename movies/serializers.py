from rest_framework import serializers
from .models import Movie, Genre


<<<<<<< HEAD
class GenreSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)  
=======
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
>>>>>>> f017fb2bdc19ce0f06413ed1af12417451952a53

    class Meta:
        model = Movie
        fields = [
            'id',
<<<<<<< HEAD
            'title',
            'genres',
=======
            'title',      
>>>>>>> f017fb2bdc19ce0f06413ed1af12417451952a53
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