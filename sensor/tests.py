from django.test import TestCase
from .models import Sensor
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

class SensorModelTest(TestCase):

    def setUp(self):
        # Happy Path:this involves Setting up a valid Sensor instance for testing
        self.sensor = Sensor.objects.create(
            Type="Waterpressure",
            Location="Nairobi",
            Status="Active",
            Time_Date=timezone.now().date()  
        )

    def test_sensor_creation(self):
        # Happy Path:  this Ensures that  Sensor is created correctly with all valid fields
        sensor = Sensor.objects.get(Sensor_ID=self.sensor.Sensor_ID)
        self.assertEqual(sensor.Type, "Waterpressure")
        self.assertEqual(sensor.Location, "Nairobi")
        self.assertEqual(sensor.Status, "Active")
        self.assertEqual(sensor.Time_Date, self.sensor.Time_Date)

    def test_sensor_string_representation(self):
        # Happy Path:  this Ensures that the string representation of the Sensor is correct
        self.assertEqual(str(self.sensor), f"Sensor {self.sensor.Sensor_ID} - Waterpressure")

    def test_default_location(self):
        # Happy Path:  It involves Creating  a Sensor without specifying Location,  it verify default value
        default_sensor = Sensor.objects.create(
            Type="Water Pressure",
            Status="Inactive"
        )
        self.assertEqual(default_sensor.Location, "karen")

    def test_sensor_creation_missing_type(self):
        # Unhappy Path:  this Verify IntegrityError is raised if Type is missing
        with self.assertRaises(IntegrityError):
            Sensor.objects.create(
                Type=None,  # Missing Type
                Location="Karen",
                Status="Active"
            )

    def test_sensor_creation_missing_status(self):
        # Unhappy Path:  this here Verify IntegrityError is raised if Status is missing
        with self.assertRaises(IntegrityError):
            Sensor.objects.create(
                Type="Waterpressure",
                Location="Nasra",
                Status=None  
            )

    def test_sensor_creation_invalid_location(self):
        # Unhappy Path: this  Verify ValidationError is raised for invalid Location
        with self.assertRaises(ValidationError):
            sensor = Sensor(
                Type="Waterpressure",
                Location='Karen' * 300,  
                Status="Active"
            )
            sensor.full_clean()  

    def test_sensor_creation_invalid_type(self):
        # Unhappy Path:  this here Verify ValidationError is raised for invalid Type
        with self.assertRaises(ValidationError):
            sensor = Sensor(
                Type='waterlevel' * 300, 
                Location="Nasra",
                Status="Active"
            )
            sensor.full_clean()  
