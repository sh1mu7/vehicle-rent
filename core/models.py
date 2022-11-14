from datetime import datetime, timedelta
import jwt
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from core import constants
from core.manager import MyUserManager
from .base import BaseModel


class Country(BaseModel):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    phone_code = models.CharField(_("Phone code"), max_length=50)
    flag = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Address(BaseModel):
    house_no = models.CharField(max_length=30)
    street = models.TextField(max_length=100)
    city = models.TextField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.country


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(unique=True, max_length=20)
    dob = models.DateField()
    image = models.ImageField(null=True)
    gender = models.SmallIntegerField(choices=constants.GenderChoices.choices, default=constants.GenderChoices.MALE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True)
    is_verified = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(blank=True)
    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    @cached_property
    def get_country_name(self):
        return self.address.country.name

    @property
    def car(self):
        return self.carinformation_set.all()

    @property
    def token(self):
        token = jwt.encode({'email': self.email, 'exp': datetime.utcnow() + timedelta(hours=24)}, settings.SECRET_KEY,
                           algorithm='HS256')
        return token


class CarInformation(BaseModel):
    user = models.ForeignKey('core.User', on_delete=models.CASCADE)
    brand = models.CharField(max_length=100, blank=False,null=False)
    model = models.CharField(max_length=100, blank=False,null=False)
    number_plate = models.CharField(max_length=10)

    def __str__(self):
        return self.number_plate
