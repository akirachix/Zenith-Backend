from django.db import models
from django.contrib.auth.models import User as DjangoUser

Estate_Associate = "Estate_Associate"
ADMIN = "ADMIN"
ROLE_CHOICES = [
    (Estate_Associate, "Estate_Associate"),
    (ADMIN, "ADMIN"),
]


class User(models.Model):
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)
    role = models.CharField(
        max_length=30,
        choices=ROLE_CHOICES,
        default=Estate_Associate,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
