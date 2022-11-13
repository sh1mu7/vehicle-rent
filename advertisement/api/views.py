from rest_framework.viewsets import ModelViewSet
from advertisement.permissions import IsCreationOrIsAuthenticated
from advertisement.api import serializers
from advertisement.models import Advertisement


class AdvertisementAPI(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = serializers.AdvertisementSerializer
    permission_classes = [IsCreationOrIsAuthenticated]
