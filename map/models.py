from django.db import models



class Device(models.Model):
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    status = models.CharField(max_length=255, null=False, blank=False)
    type = models.CharField(max_length=50, default="sensor")

    def __str__(self):
        return f"{self.type} - {self.address}"
