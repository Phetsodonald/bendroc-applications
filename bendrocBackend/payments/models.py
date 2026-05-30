from django.db import models


class Payment(models.Model):
    STATUS_CHOICE = [
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("failed", "Failed"),
    ]

    application = models.OneToOneField(
        "applications.Application",
        on_delete=models.CASCADE
    )


    amount = models.DecimalField(
        max_digits=10,
          decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICE,
        default="pending"
    )

    reference = models.CharField(
        max_length=255,
        unique=True
    )

    paid_at = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.reference