from django.db import models 
from datetime import date
from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from uuid import uuid4

# date validation
def only_future_date(value):
        today = date.today()
        if value <= today:
            raise ValidationError('Date must be a future date.')


# Create your models here.

class GeoPoint (models.Model):
    latitude = models.DecimalField( max_digits=10 , decimal_places=8, validators= [ 
        MaxValueValidator(+90.00000000),
        MinValueValidator(-90.00000000)], 
        error_messages= 'Latitude value between +90.00000000 and -90.00000000')

    longitude = models.DecimalField( max_digits=11 , decimal_places=8, validators= [ 
        MaxValueValidator(+180.00000000),
        MinValueValidator(-180.00000000)], 
        error_messages= "Longitude value between +180.00000000 and -180.00000000")

    #event = models.ForeignKey('Event', on_delete= models.CASCADE, primary_key=True)
    
 

class Event (models.Model):
    #geo_point = models.ForeignKey(GeoPoint, on_delete= models.CASCADE,primary_key=True, related_name='Event')
    geo_point = models.OneToOneField(GeoPoint, on_delete= models.CASCADE, primary_key=True)
    date = models.DateField(help_text="Enter a future date ", validators=[only_future_date])
    
    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title 


class EventAll(models.Model):
    latitude = models.DecimalField( max_digits=10 , decimal_places=8, validators= [ 
        MaxValueValidator(+90.00000000),
        MinValueValidator(-90.00000000)], 
        error_messages= 'Latitude value between +90.00000000 and -90.00000000')

    longitude = models.DecimalField( max_digits=11 , decimal_places=8, validators= [ 
        MaxValueValidator(+180.00000000),
        MinValueValidator(-180.00000000)], 
        error_messages= "Longitude value between +180.00000000 and -180.00000000")

    date = models.DateField(help_text="Enter a future date ", validators=[only_future_date]) 
     
    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title 