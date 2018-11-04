from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('analyze/', views.analyze, name='analyze'),
    path('analyze/common-area', views.common_area, name='cpa'),
    path('analyze/common-times', views.common_time, name='analyze'),

    path('analyze/highest-pay', views.analyze, name='analyze'),
    path('analyze/drivers/', views.drivers, name='analyze'),
    path('analyze/drivers/<str:driver_id>', views.driver, name='analyze'),

    path('analyze/top-earners/', views.analyze, name='analyze'),
    path('analyze/cars/', views.cars, name='analyze'),
    path('analyze/cars/<str:car_id>', views.car, name='analyze'),
    path('analyze/top-drove/', views.analyze, name='analyze'),

]
