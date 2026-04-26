from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, GenreViewSet


router = DefaultRouter()

# ENDPOINTS
router.register('movies', MovieViewSet, basename='movies')
router.register('genres', GenreViewSet, basename='genres')

urlpatterns = router.urls