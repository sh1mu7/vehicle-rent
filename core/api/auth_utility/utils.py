
from django.core.mail import send_mail


from rest_framework_simplejwt.tokens import RefreshToken


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
