from django.urls import path
from .views import UserListView, UserDetailView, RegisterView, LoginView, RoleBasedView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MonitoringDataViewSet
from .views import DrainageSystemList, DrainageSystemDetail
from map.views import map_view
from map.views import MapDeviceListView, DeviceSearchView, map_view
from .views import SensorListCreateView, SensorDetailView
from .views import NotificationViewSet

router = DefaultRouter()
router.register(r"monitoring-data", MonitoringDataViewSet)
router = DefaultRouter()
router.register(r"notifications", NotificationViewSet)
urlpatterns = router.urls
urlpatterns = [
    path("", include(router.urls)),
    path("users/", UserListView.as_view(), name="user-list"),
    path("users/<int:id>/", UserDetailView.as_view(), name="user-detail"),
    path("users/register/", RegisterView.as_view(), name="user-register"),
    path("users/login/", LoginView.as_view(), name="user-login"),
    path("users/role-based/", RoleBasedView.as_view(), name="role-based"),
    path("", include(router.urls)),
    path(
        "drainage-systems/", DrainageSystemList.as_view(), name="drainage-system-list"
    ),
    path(
        "drainage-systems/<int:pk>/",
        DrainageSystemDetail.as_view(),
        name="drainage-system-detail",
    ),
    path("api", map_view, name="map_view"),
    path("map/", map_view, name="map_view"),
    path("devices/", MapDeviceListView.as_view(), name="device-list"),
    path("search/", DeviceSearchView.as_view(), name="device-search"),
    path("sensors/", SensorListCreateView.as_view(), name="sensor-list-create"),
    path("sensors/<int:pk>/", SensorDetailView.as_view(), name="sensor-detail"),
    path(
        "notifications/", NotificationViewSet.as_view({"get": "list", "post": "create"})
    ),
    path(
        "datamonitoring/",
        MonitoringDataViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "notifications/<int:pk>/",
        NotificationViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),
]
