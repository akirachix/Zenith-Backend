from django.urls import path
from .views import map_view
from .views import MapDeviceListView, DeviceSearchView, map_view

urlpatterns = [
    path('api', map_view, name='map_view'),  
    path('map/', map_view, name='map_view'),
    path('devices/', MapDeviceListView.as_view(), name='device-list'),
    path('search/', DeviceSearchView.as_view(), name='device-search'),
]


