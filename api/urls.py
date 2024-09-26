from django.urls import path
from .views import UserListView, UserDetailView, RegisterView, LoginView, RoleBasedView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MonitoringDataViewSet
from  .views import DrainageSystemListCreateView 
from map.views import map_view
from map.views import MapDeviceListView, DeviceSearchView, map_view
from .views import SensorListCreateView, SensorDetailView
from .views import NotificationViewSet


router = DefaultRouter()
router.register(r"monitoring-data", MonitoringDataViewSet)
router = DefaultRouter()
router.register(r"notifications", NotificationViewSet)

urlpatterns = router.urls
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserListView, UserDetailView, RegisterView, LoginView, RoleBasedView,
    MonitoringDataViewSet, DrainageSystemList, DrainageSystemDetail,
    SensorListCreateView, SensorDetailView, NotificationViewSet
)
from map.views import map_view, MapDeviceListView, DeviceSearchView


router = DefaultRouter()
router.register(r"monitoring-data", MonitoringDataViewSet)
router.register(r"notifications", NotificationViewSet)

    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:id>/', UserDetailView.as_view(), name='user-detail'),
    path('users/register/', RegisterView.as_view(), name='user-register'),
    path('users/login/', LoginView.as_view(), name='user-login'),
    path('users/role-based/', RoleBasedView.as_view(), name='role-based'),
]            
path("", include(router.urls)),
path("users/", UserListView.as_view(), name="user-list"),
path("users/<int:id>/", UserDetailView.as_view(), name="user-detail"),
path("users/register/", RegisterView.as_view(), name="user-register"),
path("users/login/", LoginView.as_view(), name="user-login"),
path("users/role-based/", RoleBasedView.as_view(), name="role-based"),
path("", include(router.urls)),

urlpatterns = [
    
    path("", include(router.urls)),
    path("users/", UserListView.as_view(), name="user-list"),
    path("users/<int:id>/", UserDetailView.as_view(), name="user-detail"),
    path("users/register/", RegisterView.as_view(), name="user-register"),
    path("users/login/", LoginView.as_view(), name="user-login"),
    path("users/role-based/", RoleBasedView.as_view(), name="role-based"),
    path("drainage-systems/", DrainageSystemList.as_view(), name="DrainageSystemList"),
    path("drainage-systems/<int:pk>/", DrainageSystemDetail.as_view(), name="DrainageSystemDetail"),
    path("api", map_view, name="map_view"),
    path("map/", map_view, name="map_view"),
    path("devices/", MapDeviceListView.as_view(), name="device-list"),
    path("search/", DeviceSearchView.as_view(), name="device-search"),
    path("sensors/", SensorListCreateView.as_view(), name="sensor-list-create"),
    path("sensors/<int:pk>/", SensorDetailView.as_view(), name="sensor-detail"),
    path("notifications/", NotificationViewSet.as_view({"get": "list", "post": "create"})),
    path("datamonitoring/", MonitoringDataViewSet.as_view({"get": "list", "post": "create"})),
    path("notifications/<int:pk>/", NotificationViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
]

    
path("api", map_view, name="map_view"),
path("map/", map_view, name="map_view"),
path("devices/", MapDeviceListView.as_view(), name="device-list"),
path("search/", DeviceSearchView.as_view(), name="device-search"),
path("sensors/", SensorListCreateView.as_view(), name="sensor-list-create"),
path("sensors/<int:pk>/", SensorDetailView.as_view(), name="sensor-detail"),
path("notifications/", NotificationViewSet.as_view({"get": "list", "post": "create"})), 
path("datamonitoring/", MonitoringDataViewSet.as_view({"get": "list", "post": "create"})),   
path("notifications/<int:pk>/", NotificationViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),)
path('api/drainage-systems/', DrainageSystemListCreateView.as_view(), name='drainage-system-list-create'),
        
    
