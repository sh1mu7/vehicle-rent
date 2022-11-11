from decouple import config
from .base import *

DEBUG = config('DEBUG', cast=bool)
SECRET_KEY = config('SECRET_KEY')

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static/']
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR / 'media')

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': config('DB_PORT', cast=int),
#         'ATOMIC_REQUESTS': True,
#     }
# }

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
# EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER='ximul61@gmail.com'
EMAIL_HOST_PASSWORD='orzvkwrxpjssnuzm'
