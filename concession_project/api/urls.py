from rest_framework_nested import routers
from django.urls import path, include
from .views import ConcessionViewSet, VehiculeViewSet

router = routers.SimpleRouter()
router.register(r'concessions', ConcessionViewSet)

vehicule_router = routers.NestedSimpleRouter(router, r'concessions', lookup='concession')
vehicule_router.register(r'vehicules', VehiculeViewSet, basename='concession-vehicules')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(vehicule_router.urls)),
]