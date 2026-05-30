from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = [
        ("admin", "admin"),
        ("agent", "agent"),
        ("client", "client")
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="client"
                            
    )