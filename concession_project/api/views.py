from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Concession, Vehicule
from .serializers import ConcessionReadSerializer, ConcessionWriteSerializer, VehiculeSerializer

class ConcessionViewSet(viewsets.ModelViewSet):
    queryset = Concession.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ConcessionReadSerializer
        return ConcessionWriteSerializer

class VehiculeViewSet(viewsets.ModelViewSet):
    queryset = Vehicule.objects.all()
    serializer_class = VehiculeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['marque', 'date_mise_en_service', 'concession']

    def get_queryset(self):
        """
        Filtrer les véhicules en fonction de la concession si elle est spécifiée dans l'URL.
        """
        concession_id = self.kwargs.get('concession_pk')
        if concession_id:
            return Vehicule.objects.filter(concession_id=concession_id)
        return super().get_queryset()