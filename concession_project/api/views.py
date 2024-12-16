from rest_framework import viewsets
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