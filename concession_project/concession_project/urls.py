from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Inclut les routes de l'API
    path('', RedirectView.as_view(url='/api/', permanent=True)),  # Redirection de `/` vers `/api/`
]