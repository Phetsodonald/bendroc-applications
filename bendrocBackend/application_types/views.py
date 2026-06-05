from rest_framework import generics

from .models import ApplicationType
from .serializers import ApplicationTypeSerializer


class ApplicationTypeListView(generics.ListAPIView):
    queryset = ApplicationType.objects.filter(is_active=True)
    serializer_class = ApplicationTypeSerializer