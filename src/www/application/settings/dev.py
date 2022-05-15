"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1o3on#t%fz71n-2v^!o((c(8j-*a^!@f5b3+2youf75go(re#c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'notasquare.urad_api.apps.NotasquareUradApiConfig',
    'application.apps.ApplicationConfig',
    #'django.contrib.admin',
    #'django.contrib.auth',
    #'django.contrib.contenttypes',
    #'django.contrib.sessions',
    #'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE_CLASSES = [
    #'django.middleware.security.SecurityMiddleware',
    #'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    #'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'application.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'application/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                #'django.contrib.auth.context_processors.auth',
                #'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'application.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':    'django.db.backends.mysql',
        'NAME':      'api_db',
        'USER':      'root',
        'PASSWORD':  '123456',
        'HOST':      os.environ.get("MYSQL_PORT_3306_TCP_ADDR", None),
        'PORT':      os.environ.get("MYSQL_PORT_3306_TCP_PORT", None)
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

# Logger
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level':      'DEBUG',
            'class':      'logging.FileHandler',
            'filename':   '/opt/debug.log'
        }
    },
    'loggers': {
        'default': {
            'handlers':   ['file'],
            'level':      'DEBUG',
            'propagate':  True
        }
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

NOTASQUARE_URAD_CONTAINER = 'application.modules.common.containers.Container'
NOTASQUARE_URAD_TEST_CONTAINER = 'application.modules.common.containers.Container'
NOTASQUARE_RBAC_AUTHORIZATOR_SECURITY_CLASS = 'application.security'
NOTASQUARE_CONSUMERS_CONFIG_CLASS = 'application.consumers'
NOTASQUARE_MAX_ACTIVE_CONSUMERS = 10

#Single sign on
OAUTH_CLIENT_EK = 'DD52AFE1658490C7D5824E0E61F915D4AB104452'
OAUTH_EXPIRE_TIME = 3*24*60*60 # 3 days



# S3
AWS_ACCESS_KEY_ID='AKIAINK6TVPLDQ4R6YQA'
AWS_SECRET_ACCESS_KEY='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'
AWS_S3_BUCKET='dev-nb-fashion-data-api'