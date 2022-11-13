from django.urls import path
from rest_framework import routers
from ..api import views

app_name = 'core_api'

router = routers.DefaultRouter()
# router.register(r'users', views.UserList)
# router.register(r'country', views.CountryList)
router.register(r'car', views.CarAPI)

urlpatterns = [
    path('register', views.RegisterAPI.as_view(), name='user-register'),
    path('email_verification', views.UserVerifyApi.as_view(), name='email-verification'),
    path('login', views.LoginAPI.as_view(), name='login')

]
urlpatterns += router.urls
