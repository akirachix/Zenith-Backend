from django.urls import path
from .views import UserListView, UserDetailView, RegisterView, LoginView, RoleBasedView

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MonitoringDataViewSet
from .views import DrainageSystemList, DrainageSystemDetail

router = DefaultRouter()
router.register(r'monitoring-data', MonitoringDataViewSet)

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:id>/', UserDetailView.as_view(), name='user-detail'),
    path('users/register/', RegisterView.as_view(), name='user-register'),
    path('users/login/', LoginView.as_view(), name='user-login'),
    path('users/role-based/', RoleBasedView.as_view(), name='role-based'),
    path('', include(router.urls)),
    path('drainage-systems/', DrainageSystemList.as_view(), name='drainage-system-list'),
    path('drainage-systems/<int:pk>/', DrainageSystemDetail.as_view(), name='drainage-system-detail'),
]