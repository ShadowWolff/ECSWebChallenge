from django.urls import path, include

from . import views

urlpatterns = [

    path( '/cash_card/<str:type>/<str:id>', views.cash_card, name="cash_card" ),

    path( '/routes_count/<str:type>/<str:id>/', views.nr_of_routes, name="routes" ),
    path( '/routes_count/<str:type>/<str:id>/<str:start>/<str:finish>', views.nr_of_routes, name="routes" ),
    path( '/routes/<str:car_id>', views.car_routes, name="car_routes"),
    path( '/routes/', views.car_routes, name="car_routes"),

    path( '/general/', views.general, name="common_time" )

]
