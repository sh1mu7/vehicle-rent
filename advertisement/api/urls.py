from django.urls import path
from rest_framework import routers

from advertisement.api import views

app_name = 'advertisement'
router = routers.DefaultRouter()
router.register(r'', views.AdvertisementAPI)

urlpatterns = [
]

urlpatterns += router.urls
