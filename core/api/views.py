import jwt
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from . import serializers
from rest_framework.viewsets import ModelViewSet
from core.models import User, Country, CarInformation
from rest_framework import permissions, status, viewsets
from .auth_utility.utils import send_verification_email
from .serializers import LoginSerializer


# class UserList(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserSerializer


# class CountryList(ModelViewSet):
#     queryset = Country.objects.all()
#     serializer_class = serializers.CountrySerializer


class RegisterAPI(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        serializer = serializers.RegisterSerializer(data=request.data, context={"request": self.request})
        if serializer.is_valid():
            user = serializer.save()
            current_site = get_current_site(request).domain
            token = RefreshToken.for_user(user).access_token
            reverse_url = reverse('api-v1:email-verification')
            data = {
                'email': user.email,
                'url': 'http://' + current_site + reverse_url + '?token=' + str(token)
            }
            send_verification_email(data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserVerifyApi(APIView):
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email': 'Successfully Activated'}, status=status.HTTP_201_CREATED)
        except jwt.ExpiredSignatureError:
            return Response({'error': 'Token Error'}, status=status.HTTP_201_CREATED)
        except jwt.DecodeError:
            return Response({'error': 'Invalid Token'}, status=status.HTTP_400_BAD_REQUEST)


class LoginAPI(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=email, password=password)
        if user:
            serializer = LoginSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': "Invalid Credential"}, status=status.HTTP_401_UNAUTHORIZED)


class CarAPI(ModelViewSet):
    queryset = CarInformation.objects.all()
    serializer_class = serializers.CarSerializer
