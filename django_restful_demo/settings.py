# coding:utf-8
"""
Django settings for django_restful_demo project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(_)0u@2r3=6e&7r8r$y-$+(%enu5vb1oo5bbbmpf7=o0726m70'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'day01.apps.Day01Config',
    'day02.apps.Day02Config',
    'day03.apps.Day03Config',
    'day03_1',
    'day04.apps.Day04Config',
    'day05.apps.Day05Config',
    'day06.apps.Day06Config',
    'day06_1',
    'day07.apps.Day07Config',
    'day08'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_restful_demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'django_restful_demo.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

# # day03_1
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': ['day03_1.utils.auth.TestAuthentication']
# }
#
# # day04
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': ['day03_1.utils.auth.TestAuthentication']
# }


# # day07
# REST_FRAMEWORK = {
#     "DEFAULT_AUTHENTICATION_CLASSES": ['day07.utils.auth.Authentication', ],
#     "DEFAULT_PERMISSION_CLASSES": ['day07.utils.permission.SVIPPermission', ],
#     "UNAUTHENTICATED_USER": lambda: "匿名用户",
#     "UNAUTHENTICATED_USER": None,
#
# }


# from day06_1.utils.permission import TestPermission

# # day06_1
# REST_FRAMEWORK = {
#     'UNAUTHENTICATED_USER': None,
#     'UNAUTHENTICATED_TOKEN': None,
#     "DEFAULT_AUTHENTICATION_CLASSES": [
#         "day06_1.utils.authentication.TestAuthentication",
#     ],
#     "DEFAULT_PERMISSION_CLASSES": [
#         "day06_1.utils.permission.TestPermission",
#     ],
# }


# day08
REST_FRAMEWORK = {
    "DEFAULT_THROTTLE_RATES": {
        "Luffy": '1/s',
        "anon": '1/s',
    }
}
