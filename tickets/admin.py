from django.contrib import admin
from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    # NUEVO: columnas visibles en admin
    list_display = (
        'id',
        'showtime',
        'customer_name',
        'seats',
        'created_at',
    )

    # NUEVO: búsqueda por cliente
    search_fields = ('customer_name',)

    # NUEVO: filtros laterales
    list_filter = ('showtime', 'created_at')