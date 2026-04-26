from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, GenreViewSet

router = DefaultRouter()
<<<<<<< HEAD
router.register(r'movies', MovieViewSet)
router.register(r'genres', GenreViewSet)
=======
router.register('movies', MovieViewSet, basename='movies')
router.register('genres', GenreViewSet, basename='genres')
>>>>>>> f017fb2bdc19ce0f06413ed1af12417451952a53

urlpatterns = router.urls