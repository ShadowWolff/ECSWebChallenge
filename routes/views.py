from django.shortcuts import render
from django.db.models import Sum
from .models import RoutesModel
# Create your views here.


def home( request ):
    context = {}
    return render( request, "html/home.html", context )


def analyze(request):
    context = {}
    return render( request, "html/analyze_homepage.html", context )


def drivers(request):
    drivers_dict = {}
    routes = RoutesModel.objects.all().order_by("pickup_datetime")

    for route in routes:

        possible_driver = drivers_dict.get(str(route.driver_id))

        if possible_driver == None:

            driver_stats = {
                "driver_id": route.driver_id,
                "nr_of_routes": 1,
                "first_route": route.pickup_datetime
            }

            drivers_dict[str(route.driver_id)] = driver_stats
        else:
            possible_driver["nr_of_routes"] = possible_driver["nr_of_routes"] + 1


    context = {
        "drivers" : drivers_dict
    }
    return render(request, "html/all_drivers.html", context)


def driver(request, driver_id):
    routes = RoutesModel.objects.all().filter(driver_id = driver_id)

    cars = routes.order_by("pickup_datetime")
    longest_routes = routes.order_by("trip_distance")

    context = {
        "driver_id" : driver_id,
        "cars" : cars,
        "routes" : longest_routes,
    }
    return render(request, "html/driver.html", context)


def cars(request):
    # cars = RoutesModel.objects.values("car_id").annotate( km_driver=Sum("trip_distance") ).order_by("-trip_distance")[:5]
    cars_dict = {}

    routes = RoutesModel.objects.all().order_by("pickup_datetime")

    for route in routes:
        possible_car = cars_dict.get(str(route.car_id))

        if possible_car == None:

            car_stats = {
                "car_id": route.car_id,
                "nr_of_routes": 1,
                "km_drove" : route.trip_distance,
                "first_route": route.pickup_datetime,
                "drivers" : [ route.driver_id ],
                "nr_of_drivers" : 1
            }

            cars_dict[str(route.car_id)] = car_stats
        else:
            possible_car["nr_of_routes"] = possible_car["nr_of_routes"] + 1
            possible_car["km_drove"] = possible_car["km_drove"] + route.trip_distance
            if route.driver_id not in possible_car["drivers"]:
                possible_car["drivers"].append(route.driver_id)
                possible_car["nr_of_drivers"] = possible_car["nr_of_drivers"] + 1


    context = {
        "cars" : cars_dict
    }
    return render(request, "html/all_cars.html", context)


def car( request, car_id ):
    routes = RoutesModel.objects.filter(car_id=car_id)
    drivers = routes.order_by("pickup_datetime")
    longest_routes = routes.order_by("trip_distance")

    context = {
        "car_id" : car_id,
        "drivers" : drivers,
        "routes" : longest_routes,
    }
    return render(request, "html/car.html", context)


def common_area( request ):
    return render( request, "html/cpa.html", {} )


def routes(request):
    routes = RoutesModel.objects.all()
    context = {
        "routes" : routes
    }
    return render(request, "html/routes.html", context)


def route(request, route_id):
    route = RoutesModel.objects.all().get(id=route_id)
    context = {
        "route": route
    }
    return render(request, "html/route.html", context)


def pay(request):
    return render(request, "html/highest_pay.html", {})