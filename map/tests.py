from django.test import TestCase
from django.db import IntegrityError
from map.models import Device


class DeviceModelTest(TestCase):
    def setUp(self):
        self.device = Device.objects.create(
            address="123 Nairobi Street",
            latitude=-1.286389,
            longitude=36.817223,
            status="active",
            type="sensor",
        )

    def test_device_creation(self):
        device = self.device
        self.assertIsInstance(device, Device)
        self.assertEqual(device.address, "123 Nairobi Street")
        self.assertEqual(device.latitude, -1.286389)
        self.assertEqual(device.longitude, 36.817223)
        self.assertEqual(device.status, "active")
        self.assertEqual(device.type, "sensor")

    def test_device_str_method(self):
        device = self.device
        expected_str = f"{device.type} - {device.address}"
        self.assertEqual(str(device), expected_str)

    def test_empty_address_field(self):
        Device.objects.create(
            address="",
            latitude=-1.286389,
            longitude=36.817223,
            status="active",
            type="sensor",
        )

    def test_missing_latitude_field(self):
        with self.assertRaises(IntegrityError):
            Device.objects.create(
                address="456 Another Street",
                latitude=None,
                longitude=36.817223,
                status="active",
                type="sensor",
            )

    def test_invalid_latitude_value(self):
        with self.assertRaises(ValueError):
            Device.objects.create(
                address="789 Invalid Lat Street",
                latitude="invalid_latitude",
                longitude=36.817223,
                status="active",
                type="sensor",
            )

    def test_empty_status_field(self):
        Device.objects.create(
            address="999 Status Street",
            latitude=-1.286389,
            longitude=36.817223,
            status="",
            type="sensor",
        )
