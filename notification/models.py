from django.db import models

NOTIFICATION_TYPES = [
    ('info', 'Information'),
    ('warn', 'Warning'),
    ('error', 'Error'),
    ('success', 'Success'),
]
class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    message = models.TextField()
    type = models.CharField(max_length=255, choices=NOTIFICATION_TYPES)
    created_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
# Create your models here.
