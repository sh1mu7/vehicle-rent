from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from advertisement.api import serializers
from advertisement.models import Advertisement


class AdvertisementAPI(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = serializers.AdvertisementSerializer
    permission_classes = [IsAuthenticated]
