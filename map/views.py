import os
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from map.models import Device
from .serializers import DeviceSerializer
from django.shortcuts import render
from .models import Device

# Load API key from environment variable
GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')
GEOCODE_URL = 'https://maps.googleapis.com/maps/api/geocode/json'


def map_view(request):
    devices = list(Device.objects.values('latitude', 'longitude', 'address', 'status'))
    return render(request, 'map/map_template.html', {'devices': devices})

class MapDeviceListView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    
    def post(self, request):
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeviceSearchView(APIView):
    def get(self, request):
        latitude = request.query_params.get('latitude')
        longitude = request.query_params.get('longitude')

        if not latitude or not longitude:
            return Response({'error': 'Latitude and Longitude are required'}, status=status.HTTP_400_BAD_REQUEST)
            
        try:
            latitude = float(latitude)
            longitude = float(longitude)
            nearby_devices = Device.objects.filter(
                latitude__range=(latitude - 0.01, latitude + 0.01),
                longitude__range=(longitude - 0.01, longitude + 0.01)
            )
            serializer = DeviceSerializer(nearby_devices, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError:
            return Response({'error': 'Invalid latitude or longitude'}, status=status.HTTP_400_BAD_REQUEST)
        except requests.RequestException as e:
            return Response({'error': f'Network error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)