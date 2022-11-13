from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from core.models import Country, CarInformation
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserModel
#         fields = '__all__'
#
#     def create(self, validated_data):
#         validated_data['password'] = make_password(validated_data['password'])
#         return super(UserSerializer, self).create(validated_data)
#
#
# class CountrySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Country
#         fields = '__all__'
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarInformation
        fields = "__all__"
        depth = 1


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    car = CarSerializer(many=True)

    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'dob', 'email', 'mobile', 'password', 'confirm_password',
                  'address', 'gender', 'car']
        read_only_fields = ['car']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({'confirm_password': [_("Passwords do not match"), ]})
        print(data['car'])
        return data

    def create(self, validated_data):
        confirm_password = validated_data.pop('confirm_password')
        car = validated_data.pop('car')
        print(car)
        user = UserModel.objects.create(**validated_data)
        user.set_password(confirm_password)
        user.save()
        for car in car:
            CarInformation.objects.create(**car, user=user)
        return user


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = UserModel
        fields = ['email', 'password', 'token']
        read_only_fields = ['token']


class PasswordChangeSerializer(serializers.ModelSerializer):
    model = UserModel

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
