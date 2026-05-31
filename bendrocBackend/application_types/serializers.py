from rest_framwork import serializers
from .models import ApplicationType


class ApplicationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationType
        fields = "__all__"