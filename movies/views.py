from rest_framework import viewsets
from .models import Movie, Genre
from .serializers import MovieSerializer, GenreSerializer


class GenreViewSet(viewsets.ModelViewSet):
    # NUEVO: CRUD completo para géneros
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    # CRUD completo para películas
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.all()

        # BÚSQUEDA POR TÍTULO
        title = self.request.query_params.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title)

        # FILTRO POR ESTADO ACTIVO
        is_active = self.request.query_params.get('is_active')
        if is_active is not None:
            queryset = queryset.filter(is_active=is_active.lower() == 'true')

        # FILTRO POR GÉNERO USANDO ID
        genre_id = self.request.query_params.get('genre')
        if genre_id:
            queryset = queryset.filter(genres__id=genre_id)

        # FILTRO POR NOMBRE DE GÉNERO
        genre_name = self.request.query_params.get('genre_name')
        if genre_name:
            queryset = queryset.filter(genres__name__icontains=genre_name)

        # FILTRO POR DURACIÓN MÍNIMA
        min_duration = self.request.query_params.get('min_duration')
        if min_duration:
            queryset = queryset.filter(duration__gte=min_duration)

        # FILTRO POR DURACIÓN MÁXIMA
        max_duration = self.request.query_params.get('max_duration')
        if max_duration:
            queryset = queryset.filter(duration__lte=max_duration)

        # ORDENAMIENTO
        ordering = self.request.query_params.get('ordering')
        allowed_ordering_fields = [
            'title',
            '-title',
            'duration',
            '-duration',
            'release_date',
            '-release_date',
            'created_at',
            '-created_at',
        ]

        if ordering in allowed_ordering_fields:
            queryset = queryset.order_by(ordering)

        # IMPORTANTE: evita películas repetidas cuando se filtra por ManyToMany
        return queryset.distinct()