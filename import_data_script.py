import csv
import os
import numpy as np
import matplotlib.pyplot as plt

import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datasight.settings')
django.setup()

from routes.models import RoutesModel


def process( row ):
    car           = row[0]
    driver_id     = row[1]
    payment_type  = row[2]
    total_amount  = row[3]
    pickup        = row[4]
    dropoff       = row[5]
    passengers    = row[6]
    trip_duration = row[7]
    trip_distance = row[8]
    pickup_long   = row[9]
    pickup_lat    = row[10]
    dropoff_long  = row[11]
    dropoff_lat   = row[12]

    r = RoutesModel(
        driver_id = driver_id,
        car_id = car,
        payment_type = payment_type,
        total_amount = total_amount,
        pickup_datetime = pickup,
        dropoff_datetime = dropoff,
        passengers = passengers,
        trip_duration = trip_duration,
        trip_distance = trip_distance,
        pickup_long =pickup_long,
        pickup_lat = pickup_lat,
        dropoff_long = dropoff_long,
        dropoff_lat = dropoff_lat
    )

    r.save()

with open( "data_final.csv" ) as f:
    csv_reader = csv.reader( f )
    i = 0
    x = np.empty((1,10), dtype=float)
    y = np.empty((1,10), dtype=float)

    for row in csv_reader:

        if i != 0:
            # process(row)
            np.append(x, float(row[9]))
            np.append(y, float(row[10]))

        i = i+1
        if i >10000:
            break

plt.scatter(x,y)
plt.show()