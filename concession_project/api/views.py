from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Concession, Vehicule
from .serializers import ConcessionReadSerializer, ConcessionWriteSerializer, VehiculeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.reverse import reverse

class ConcessionViewSet(viewsets.ModelViewSet):
    # ViewSet pour gérer les concessions
    queryset = Concession.objects.all()

    def get_serializer_class(self):
        # Retourne un serializer différent selon l'action effectuée
        if self.action in ['list', 'retrieve']:
            return ConcessionReadSerializer
        return ConcessionWriteSerializer

class VehiculeViewSet(viewsets.ModelViewSet):
    # ViewSet pour gérer les véhicules
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

class APIRootView(APIView):
    """
    Vue racine pour retourner les endpoints principaux de l'API.
    """
    def get(self, request, *args, **kwargs):
        return Response({
            'concessions': reverse('concession-list', request=request),
            'vehicules': reverse('concession-vehicules-list', request=request, kwargs={'concession_pk': 1}),
        })