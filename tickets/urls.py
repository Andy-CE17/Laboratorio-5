from rest_framework.routers import DefaultRouter
from .views import TicketViewSet


router = DefaultRouter()

# NUEVO: endpoint de tickets
router.register('tickets', TicketViewSet, basename='tickets')

urlpatterns = router.urls