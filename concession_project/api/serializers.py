from rest_framework import serializers
from .models import Concession, Vehicule

class ConcessionReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concession
        fields = ['id', 'nom', 'code_postal', 'adresse']

class ConcessionWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concession
        fields = ['id', 'nom', 'code_postal', 'adresse', 'numero_siret']

class VehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicule
        fields = ['id', 'marque', 'modele', 'chevaux', 'immatriculation', 'date_mise_en_service', 'concession']