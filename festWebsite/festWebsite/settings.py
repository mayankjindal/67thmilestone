"""
Django settings for festWebsite project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(__file__)
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '12!hq_-1ivucrim@+emw2_q+udvh+bhpbhwe!vd&^m9+k5lw)d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'festWebsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'festWebsite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bmldb',
        'USER': 'u_bml',
        'PASSWORD': 'Nishit@30',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_USE_TLS = True
EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.zoho.com'
# EMAIL_HOST_USER = 'campus_ambassador@67thmilestone.com'
# EMAIL_HOST_PASSWORD = 'TFYnRgcF9K4x'
EMAIL_HOST_USER = 'contact@67thmilestone.com'
EMAIL_HOST_PASSWORD = 'KrTzvfqw4XSp'
EMAIL_PORT = 465
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR, ]
MEDIA_DIR = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# """
# Django settings for festWebsite project.
#
# Generated by 'django-admin startproject' using Django 1.11.5.
#
# For more information on this file, see
# https://docs.djangoproject.com/en/1.11/topics/settings/
#
# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/1.11/ref/settings/
# """
#
# import os
#
# # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(__file__)
# TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
#
# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/
#
# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '12!hq_-1ivucrim@+emw2_q+udvh+bhpbhwe!vd&^m9+k5lw)d'
#
# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
#
# ALLOWED_HOSTS = ['*']
#
#
# # Application definition
#
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'website',
# ]
#
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]
#
# ROOT_URLCONF = 'festWebsite.urls'
#
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [TEMPLATE_DIR, ],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.template.context_processors.media',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
#
# WSGI_APPLICATION = 'festWebsite.wsgi.application'
#
#
# # Database
# # https://docs.djangoproject.com/en/1.11/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
#
#
# # Password validation
# # https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
#
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]
# EMAIL_BACKEND= "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_USE_SSL = True
# EMAIL_HOST = 'smtp.zoho.com'
# # EMAIL_HOST_USER = 'campus_ambassador@67thmilestone.com'
# # EMAIL_HOST_PASSWORD = 'TFYnRgcF9K4x'
# EMAIL_HOST_USER = 'contact@67thmilestone.com'
# EMAIL_HOST_PASSWORD = 'KrTzvfqw4XSp'
# EMAIL_PORT = 465
# # DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
#
# # APPEND_SLASH=False
#
# # Internationalization
# # https://docs.djangoproject.com/en/1.11/topics/i18n/
#
# LANGUAGE_CODE = 'en-us'
#
# TIME_ZONE = 'UTC'
#
# USE_I18N = True
#
# USE_L10N = True
#
# USE_TZ = True
#
#
# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/1.11/howto/static-files/
#
# STATIC_URL = '/static/'
# STATIC_DIR = os.path.join(BASE_DIR,'static')
# STATICFILES_DIRS = [STATIC_DIR,]
# MEDIA_DIR = os.path.join(BASE_DIR,'media')
# MEDIA_ROOT = MEDIA_DIR
# MEDIA_URL = '/media/'
# STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
