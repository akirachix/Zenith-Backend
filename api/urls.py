from django.urls import path
from .views import DrainageSystemList, DrainageSystemDetail

urlpatterns = [
    path('drainage-systems/', DrainageSystemList.as_view(), name='drainage-system-list'),
    path('drainage-systems/<int:pk>/', DrainageSystemDetail.as_view(), name='drainage-system-detail'),
]