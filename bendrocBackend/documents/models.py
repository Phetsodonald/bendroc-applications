from django.db import models


class Document(models.Model):

    application = models.ForeignKey(
        "applications.Application",
        on_delete=models.CASCADE,
        related_name="documents"
    )

    file = models.FileField(
        upload_to="documents"
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.file.name
