from django.db import models
from django.db import models
# from django.utils import timezone

class Sensor(models.Model):
    Sensor_ID = models.AutoField(primary_key=True) 
    Type = models.CharField(max_length=255) 
    Location=models.CharField(max_length=255,default='karen')       
    Status = models.CharField(max_length=100)   
    Time_Date=models.DateField(auto_now_add=True)              
    def __str__(self):
        return f"Sensor {self.Sensor_ID} - {self.Type}"

# Create your models here.

# Create your models here.
