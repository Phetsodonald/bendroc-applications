from django.db import models
from django.conf import settings


class Application(models.Model):

    STATUS_CHOICE = [
        ("draft", "Draft"),
        ("awaiting_payment", "Awaiting Payment"),
        ("paid", "Paid"),
        ("under_review", "Under Review"),
        ("submitted", "Submitted"),
        ("approved", "Approved"),
        ("rejected", "Rejected")
    ]

    user = models.ForeignKey(
        settings.Auth_USER_MODEL,
        on_delete=models.CASCADE
    )

    application_type = models.ForeignKey(
        "application_type.ApplicationType", 
        on_delete=models.PROTECT
    )

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICE,
        default="draft"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.application_type.name}"
