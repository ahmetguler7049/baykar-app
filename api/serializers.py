from rest_framework import serializers
from .models import AircraftInventory, PartInventory

class AircraftInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AircraftInventory
        fields = ['id', 'name', 'part', 'quantity']

class PartInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PartInventory
        fields = ['id', 'name', 'quantity', 'team', 'is_used']
