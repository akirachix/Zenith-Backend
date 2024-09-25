from django.db import models
class DrainageSystem(models.Model):
    Drainage_ID = models.AutoField(primary_key=True)
    Location = models.CharField(max_length=100)
    waterlevel=models.DecimalField(max_digits=10, decimal_places=2)
    waterpressure=models.DecimalField(max_digits=10, decimal_places=2)
    Status = models.CharField(max_length=100)
    Timestamp=models.DateTimeField(auto_now_add=True)
     



