from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import EventAll, Event, GeoPoint
from .serializers import EventAllSerializer, EventSerializer, GeoPointSerializer


# Create your views here.

@api_view(['GET', 'POST'])
def EventAll_list(request):
    if request.method == 'GET':
        queryset = EventAll.objects.all()
        serializer = EventAllSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EventAllSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def Event_list(request):
    if request.method == 'GET':
        queryset = Event.objects.select_related('geo_point').all()
        serializer = EventSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

            
""" class EventList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Event.objects.all()
    serializer_class =  EventSerializer

class EventCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = Event.objects.all() 
    serializer_class = EventSerializer 

class GeoPointList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = GeoPoint.objects.all()
    serializer_class =  GeoPointSerializer

class GeoPointCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = GeoPoint.objects.all() 
    serializer_class = GeoPointSerializer 

class EventAllCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = EventAll.objects.all()
    serializer_class = EventAllSerializer

class EventAllList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = EventAll.objects.all()
    serializer_class =  EventAllSerializer  """
