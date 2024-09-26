
from rest_framework import serializers
from user.models import User, ROLE_CHOICES
from django.contrib.auth.models import User 
from datamonitoring.models import MonitoringData
from drainagesystem.models import DrainageSystem
from sensor.models import Sensor
from map.models import Device
from notification.models import Notification
from user.models import User
from django.contrib.auth.models import User as DjangoUser

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'email', 'role', 'password']
        read_only_fields = ['id']

    def create(self, validated_data):
        
        django_user = DjangoUser.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        user = User.objects.create(
            user=django_user,
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            role=validated_data['role']
        )

        return user

class RoleSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    


class MonitoringDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringData
        fields = [
            "monitoring_id",
            "user_id",
            "drainage_id",
            "timestamp",
            "water_level",
            "water_pressure",
        ]


class DrainageSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrainageSystem
        fields = ['Drainage_ID', 'Location', 'waterlevel', 'waterpressure', 'Status', 'Timestamp']

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ["id", "latitude", "longitude", "address", "type"]


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ["Sensor_ID", "Type", "Location", "Status", "Time_Date"]


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ["id", "title", "message", "type", "created_at"]


