from django.urls import path
from .views import UserListView, UserDetailView, RegisterView, LoginView, RoleBasedView

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MonitoringDataViewSet

router = DefaultRouter()
router.register(r'monitoring-data', MonitoringDataViewSet)

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:id>/', UserDetailView.as_view(), name='user-detail'),
    path('users/register/', RegisterView.as_view(), name='user-register'),
    path('users/login/', LoginView.as_view(), name='user-login'),
    path('users/role-based/', RoleBasedView.as_view(), name='role-based'),
    path('', include(router.urls)),
    
]