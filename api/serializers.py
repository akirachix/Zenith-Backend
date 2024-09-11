from rest_framework import serializers
from drainagesystem.models import DrainageSystem

class DrainageSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrainageSystem
        fields = '__all__'