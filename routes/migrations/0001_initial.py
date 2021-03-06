# Generated by Django 2.1.2 on 2018-11-01 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoutesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_id', models.IntegerField()),
                ('car_id', models.IntegerField()),
                ('payment_type', models.CharField(max_length=3)),
                ('total_amount', models.FloatField()),
                ('pickup_datetime', models.DateTimeField()),
                ('dropoff_datetime', models.DateTimeField()),
                ('passengers', models.IntegerField()),
                ('trip_duration', models.IntegerField()),
                ('trip_distance', models.FloatField()),
                ('pickup_long', models.FloatField()),
                ('pickup_lat', models.FloatField()),
                ('dropoff_long', models.FloatField()),
                ('dropoff_lat', models.FloatField()),
            ],
        ),
    ]
