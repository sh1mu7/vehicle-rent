from django.urls import path, include

urlpatterns = [
    path('', include('core.api.urls', namespace='api-v1'), ),
    path('advertise', include('advertisement.api.urls', namespace='advertise'), ),

]
