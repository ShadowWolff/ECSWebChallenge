from django.db import models

# Create your models here.

class RoutesModel( models.Model ):

    driver_id        = models.IntegerField()
    car_id           = models.IntegerField()
    payment_type     = models.CharField(max_length=3)
    total_amount     = models.FloatField()

    pickup_datetime  = models.DateTimeField()
    dropoff_datetime = models.DateTimeField()

    passengers       = models.IntegerField()
    trip_duration    = models.IntegerField()
    trip_distance    = models.FloatField()

    pickup_long      = models.FloatField()
    pickup_lat       = models.FloatField()
    dropoff_long     = models.FloatField()
    dropoff_lat      = models.FloatField()
