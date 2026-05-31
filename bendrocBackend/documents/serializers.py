from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class meta:
        model = Document
        fields = "__all__"