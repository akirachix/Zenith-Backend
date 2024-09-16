# Generated by Django 5.1 on 2024-09-12 05:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("phone_number", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(max_length=16)),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("Estate_Associate", "Estate_Associate"),
                            ("ADMIN", "ADMIN"),
                        ],
                        default="Estate_Associate",
                        max_length=30,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
