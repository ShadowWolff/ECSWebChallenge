import json

from django.db.models import Count
from django.shortcuts import render, HttpResponse
from routes.models import RoutesModel

# Create your views here.

def cash_card( request, type, id ):
    data = {
        "cash" : RoutesModel.objects.all().filter(**{ type + "_id" : id }, payment_type="CSH").count(),
        "card" : RoutesModel.objects.all().filter(**{ type + "_id" : id }, payment_type="CRD").count()
    }

    json_data = json.dumps( data )

    return HttpResponse(json_data, content_type="application/json")

def nr_of_routes( request, type, id, start = None, finish = None ):
    if start == None and finish == None:
        routes = RoutesModel.objects.all().filter( **{ type + "_id" : id } )
    else:
        routes = RoutesModel.objects.all().filter( **{ type + "_id" : id }, pickup_datetime__range=(start, finish))


    dates = {}
    for r in routes:
        datetime_as_string = str( r.pickup_datetime ).split(" ")[0]
        if datetime_as_string not in dates.keys():
            dates[ datetime_as_string ] = routes.filter(
                pickup_datetime__year  =datetime_as_string.split("-")[0],
                pickup_datetime__month =datetime_as_string.split("-")[1],
                pickup_datetime__day   =datetime_as_string.split("-")[2],
            ).count()
    data = {
        "routes" : dates
    }
    json_data = json.dumps( data )
    return HttpResponse(json_data, content_type="application/json")

def car_routes( request, car_id = None ):
    if car_id != None:
        routes = RoutesModel.objects.all().filter( car_id = car_id )
    else:
        routes = RoutesModel.objects.all()
    routes_json = []
    for r in routes:
        routes_json.append(
            {
                "pickup_long" : r.pickup_long,
                "pickup_lat" : r.pickup_lat,
                "dropoff_long" : r.dropoff_long,
                "dropoff_lat" : r.dropoff_lat,
                "pass" : r.passengers,
                "pay" : r.total_amount
            }
        )
    data = {
        "routes" : routes_json
    }
    json_data = json.dumps( data )
    return HttpResponse(json_data, content_type="application/json")

def general( request ):
    general_data = {
        "pick" : [0] * 24,
        "drop" : [0] * 24,
        "pay_type" : [ {"csh" : 0, "crd": 0, "noc" : 0, "dis" : 0, "unk" : 0} for _ in range(24) ],
        "pass" : [0] * 24,
        "pass_type" : [{ "gr" : 0, "sg" : 0} for _ in range(24)],
        "payment" : [0] * 24,
        "pay_amount" : [{ "gr" : 0, "sg" : 0} for _ in range(24)],
        "pay_type_pass" : [
            { "gr" :
                  {"csh" : 0, "crd":0, "noc":0, "dis":0, "unk" :0},
              "sg" :
                  {"csh" : 0, "crd":0, "noc":0, "dis":0, "unk" :0},
            }for _ in range(24)]
    }

    routes = RoutesModel.objects.all()

    for r in routes:
        pick_hour = int( str( r.pickup_datetime ).split(" ")[1].split(":")[0] )
        drop_hour = int( str( r.dropoff_datetime ).split(" ")[1].split(":")[0] )

        general_data["pick"][pick_hour] = general_data["pick"][pick_hour] + 1
        general_data["drop"][drop_hour] = general_data["drop"][drop_hour] + 1
        general_data["pass"][pick_hour] = general_data["pass"][pick_hour] + r.passengers
        general_data["payment"][pick_hour] = general_data["payment"][pick_hour] + r.total_amount

        if r.passengers > 1:
            general_data["pass_type"][pick_hour]["gr"] = general_data["pass_type"][pick_hour]["gr"] + r.passengers
            general_data["pay_amount"][pick_hour]["gr"] = general_data["pay_amount"][pick_hour]["gr"] + r.total_amount
            general_data["pay_type_pass"][pick_hour]["gr"][r.payment_type.lower()] = general_data["pay_type_pass"][pick_hour]["gr"][r.payment_type.lower()] + r.total_amount
        else:
            general_data["pass_type"][pick_hour]["sg"] = general_data["pass_type"][pick_hour]["sg"] + 1
            general_data["pay_amount"][pick_hour]["sg"] = general_data["pay_amount"][pick_hour]["sg"] + r.total_amount
            general_data["pay_type_pass"][pick_hour]["sg"][r.payment_type.lower()] = general_data["pay_type_pass"][pick_hour]["sg"][r.payment_type.lower()] + r.total_amount

        general_data["pay_type"][pick_hour][r.payment_type.lower()] = general_data["pay_type"][pick_hour][r.payment_type.lower()] + 1

    data = {
        "data" : general_data
    }
    json_data = json.dumps( data )

    return HttpResponse(json_data, content_type="application/json")

