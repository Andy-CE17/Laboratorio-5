from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('movies.urls')),
    path('api/', include('showtimes.urls')),
    path('api/', include('tickets.urls')),
]