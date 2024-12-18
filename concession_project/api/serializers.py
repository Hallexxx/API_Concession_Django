from rest_framework import serializers
from .models import Concession, Vehicule

class ConcessionReadSerializer(serializers.ModelSerializer):
    # Serializer utilisé uniquement pour les opérations de lecture
    class Meta:
        model = Concession
        fields = ['id', 'nom', 'code_postal', 'adresse']

class ConcessionWriteSerializer(serializers.ModelSerializer):
    # Serializer utilisé uniquement pour les opérations d'écriture
    class Meta:
        model = Concession
        fields = ['id', 'nom', 'code_postal', 'adresse', 'numero_siret']

class VehiculeSerializer(serializers.ModelSerializer):
    # Serializer pour gérer tous les champs de la ressource Véhicule
    class Meta:
        model = Vehicule
        fields = ['id', 'marque', 'modele', 'chevaux', 'immatriculation', 'date_mise_en_service', 'concession']