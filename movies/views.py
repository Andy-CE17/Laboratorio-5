from rest_framework import viewsets
from .models import Movie, Genre
from .serializers import MovieSerializer, GenreSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.all()

        # BÚSQUEDA POR TÍTULO
        title = self.request.query_params.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title)

        # FILTRO POR ESTADO
        is_active = self.request.query_params.get('is_active')
        if is_active is not None:
            queryset = queryset.filter(is_active=is_active)

        # FILTRO POR GÉNERO
        genre_id = self.request.query_params.get('genre')
        if genre_id:
            queryset = queryset.filter(genres__id=genre_id)

        # ORDENAMIENTO (NUEVO)
        ordering = self.request.query_params.get('ordering')  # NUEVO
        if ordering:
            queryset = queryset.order_by(ordering)

        return queryset