from rest_framework.routers import DefaultRouter
from .views import RoomViewSet, ShowtimeViewSet

router = DefaultRouter()
router.register('rooms', RoomViewSet, basename='rooms')
router.register('showtimes', ShowtimeViewSet, basename='showtimes')

urlpatterns = router.urls