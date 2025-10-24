from rest_framework import serializers
from .models import Airport, FlightPath

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'

class FlightPathSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightPath
        fields = '__all__'
