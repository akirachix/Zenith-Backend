from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from drainagesystem.models import DrainageSystem
from api.serializers import DrainageSystemSerializer

class DrainageSystemTests(APITestCase):
    def setUp(self):
        self.drainage_system = DrainageSystem.objects.create(
            Location='karen',
            waterlevel=15.75,
            waterpressure=101.30,
            Status='Active',
        )
        self.list_url = reverse('drainage-system-list')
        self.detail_url = reverse('drainage-system-detail', kwargs={'pk': self.drainage_system.Drainage_ID})

    def test_list_drainage_systems(self):
        response = self.client.get(self.list_url)
        drainage_systems = DrainageSystem.objects.all()
        serializer = DrainageSystemSerializer(drainage_systems, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_drainage_system(self):
        data = {
            'Location': 'nasra',
            'waterlevel': 20.50,
            'waterpressure': 120.75,
            'Status': 'Inactive',
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(DrainageSystem.objects.filter(**data).exists())

    def test_create_drainage_system_invalid(self):
        data = {
            'Location': 'karen',
            'waterpressure': 120.75,
            'Status': 'Inactive',
        }
        response = self.client.post(self.list_url, data, format='json')
        print(response.data)  # Debugging output
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_drainage_system_detail(self):
        response = self.client.get(self.detail_url)
        serializer = DrainageSystemSerializer(self.drainage_system)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
