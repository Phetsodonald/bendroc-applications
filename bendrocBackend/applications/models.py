from django.conf import settings
from django.db import models


class Application(models.Model):

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("awaiting_payment", "Awaiting Payment"),
        ("paid", "Paid"),
        ("under_review", "Under Review"),
        ("submitted", "Submitted"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    application_type = models.ForeignKey(
        "application_types.ApplicationType",
        on_delete=models.PROTECT
    )

    institution_name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    programme_name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="draft"
    )

    notes = models.TextField(
        blank=True
    )

    reference_number = models.CharField(
        max_length=100,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.institution_name}"