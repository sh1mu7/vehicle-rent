from datetime import datetime, timedelta

import jwt
from django.conf import settings
from django.core.mail import send_mail
from decouple import config
from core.models import Otp
from rest_framework_simplejwt.tokens import RefreshToken


# def token_generator(user):
#     token = jwt.encode({'email': user['email'], 'exp': datetime.utcnow() + timedelta(hours=24), }, settings.SECRET_KEY,
#                        algorithms='HS256')
#     return token


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


def send_verification_email(data):
    subject = 'Verify your account'
    message = data['url']
    from_email = 'ximul61@gmail.com'
    recipient_list = [data['email']]
    send_mail(subject, message, from_email, recipient_list)
