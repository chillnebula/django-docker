from django.urls import path, include
from . import views
#from .views import   GeoPointCreate, GeoPointList ,EventList, EventCreate,EventAllCreate, EventAllList

urlpatterns = [
    
    path('Event/', views.Event_list,name='event'),
    path('Eventall/', views.EventAll_list,name='event'),

    #path('hello/', views.say_hello),
    #path('Event/create/', EventCreate.as_view(),name='create-event'),
    #path('Event/', EventList.as_view(),name = 'event-list'),

    #path('GeoPoint/create/', GeoPointCreate.as_view(), name = 'geopoint-create'),
    #path('GeoPoint/', GeoPointList.as_view(),name = 'geopoint-list'),

    #path('EventAll/create/', EventAllCreate.as_view(), name= 'eventAll-create'),
    #path('EventAll/', EventAllList.as_view(), name = 'eventAll-list'),
]
