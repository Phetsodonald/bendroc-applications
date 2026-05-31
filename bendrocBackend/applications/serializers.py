from rest_framework import serializers
from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):

    application_type_name = serializers.CharField(
        source="application_type.name",
        read_only=True
    )

    class Meta:
        model = Application
        fields = (
            "id",
            "user",
            "application_type",
            "application_type_name",
            "status",
            "created_at",
            "updated_at",
        )