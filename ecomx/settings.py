"""
Django settings for ecomx project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import django_heroku
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

from django.contrib import messages
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-f=ciu3hnc$*&6_5%p#9yeu#6$_q7m*)l1$f@7+pm=q^7-uv&in'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ecommerceapp',
    'authCart',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhitenoiseMiddleware'
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecomx.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR/'templates' ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecomx.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

#sending emails
#old way through google
EMAIL_HOST= 'smtp.gmail.com'
EMAIL_HOST_USER='faimu4584@gmail.com'
EMAIL_HOST_PASSWORD = 'njdlwfjzibozsshc'
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'

#new way
# EMAIL_HOST= 'smtpout.securenet.com'
# EMAIL_HOST_USER='xxx@yyy.com'
# EMAIL_HOST_PASSWORD = ''
# EMAIL_PORT=587
# EMAIL_USE_TLS=True
# EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'

CACHE_TTL = 60 * 5
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
]
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
#django_heroku.settings(locals())

MEDIA_URL ='/media/'
MEDIA_ROOT =os.path.join(BASE_DIR,"media")
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MESSAGE_TAGS={
    messages.ERROR:'danger'
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

PERFORMANCE_LIMITS = {
    'test method': {
        'queries': {'total': 50},  # want to keep the tests focused
        'time': {'total': 0.2},  # want fast integrated tests, so aiming for 1/5 seconds
    },
    'django.test.client.Client': {
        'queries': {
            'read': 30,
            'write': 8,  # do not create complex object structures in the web
                         # process
        },
    },
    'Template.render': {
        'queries': {
            'write': 0,  # rendering a template should never write to the database!
            'read': 0
        }
    }
}