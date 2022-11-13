from django.conf import settings
from django.db import models

from core.base import BaseModel
from core.models import CarInformation, User


# Create your models here.


class Advertisement(BaseModel):
    title = models.CharField(max_length=300, blank=False, null=False)
    description = models.TextField()
    charge_per_km = models.DecimalField(max_digits=5, decimal_places=2)
    vehicle_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title
