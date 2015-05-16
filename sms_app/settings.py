"""
Django settings for sms_app project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qfx42u61@@i^s@j^1n%^-^^*8&$(00sa4j)1b@wpavb&nj4d@@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'itisms',
        'USER': 'root',
        'PASSWORD': 'r33b00ts',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'send_sms',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sms_app.urls'

WSGI_APPLICATION = 'sms_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/home/ubuntu/tahiti-sms.com/iti_sms/iti-sms/static/'

STATICFILES_DIRS = (
    '/home/ubuntu/tahiti-sms.com/iti_sms/iti-sms/send_sms/static/css/',
    '/home/ubuntu/tahiti-sms.com/iti_sms/iti-sms/send_sms/static/img/',
    '/home/ubuntu/tahiti-sms.com/iti_sms/iti-sms/send_sms/static/js/',
)


#Templates
TEMPLATE_DIRS =(
    [os.path.join(BASE_DIR, 'templates')],
    '/home/ubuntu/tahiti-sms.com/iti_sms/iti-sms/sms_app/templates/',
    '/home/ubuntu/tahiti-sms.com/iti_sms/iti-sms/send_sms/templates/',
)

#Login/Logout
LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/messages/0'

# LOGOUT_URL = '/logout/'

try:
    from sms_app.locla_settings import *
except ImportError:
    pass