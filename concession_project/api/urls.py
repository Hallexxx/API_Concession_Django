from rest_framework_nested import routers
from django.urls import path, include
from .views import ConcessionViewSet, VehiculeViewSet, APIRootView

# Routeur principal pour gérer les concessions
router = routers.SimpleRouter()
router.register(r'concessions', ConcessionViewSet)

# Routeur imbriqué pour gérer les véhicules liés à une concession
vehicule_router = routers.NestedSimpleRouter(router, r'concessions', lookup='concession')
vehicule_router.register(r'vehicules', VehiculeViewSet, basename='concession-vehicules')

# Définition des URL pour inclure les routes principales et imbriquées
urlpatterns = [
    path('', APIRootView.as_view(), name='api-root'),
    path('', include(router.urls)),
    path('', include(vehicule_router.urls)),
]