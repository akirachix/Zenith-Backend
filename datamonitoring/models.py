from django.db import models
class MonitoringData(models.Model):
    monitoring_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)  
    drainage_id = models.IntegerField()  
    timestamp = models.DateTimeField(auto_now_add=True)  
    water_level = models.DecimalField(max_digits=10, decimal_places=2)  
    water_pressure = models.DecimalField(max_digits=10, decimal_places=2)  

    def __str__(self):
        return f'Monitoring Data {self.monitoring_id}'

