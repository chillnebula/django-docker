from .models import  GeoPoint, Event, EventAll 
from rest_framework import serializers

class GeoPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoPoint
        fields = ['latitude', 'longitude']

class EventSerializer(serializers.ModelSerializer):
    geo_point =  GeoPointSerializer(many = False)
    class Meta:
        model = Event
        fields = ['geo_point', 'date'] 

class EventAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventAll
        fields = ['latitude', 'longitude', 'date'] 