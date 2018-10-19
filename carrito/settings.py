"""
Django settings for carrito project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from django.core.urlresolvers import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'po-%ig2h#_0y+##x5&2h)u2b5#ai%1a!*7s2fbsvpe$^f6r!j('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'phonenumber_field',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app.producto',
    'app.venta',
    'app.cliente',   
    'app.caracteristicas',
    'app.subproducto',
    'app.tienda',
    'paypal.standard.ipn',
    'app.pagos',
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

ROOT_URLCONF = 'carrito.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'carrito.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'carritocompras',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',

        'OPTIONS': {
            'sql_mode': 'traditional',
        }
        
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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Mazatlan'

USE_I18N = True

USE_L10N = True

USE_TZ = True

PHONENUMBER_DB_FORMAT='E164'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS=(os.path.join(BASE_DIR, 'static'), )




MEDIA_URL = '/media/'
MEDIA_ROOT= os.path.join(BASE_DIR, 'media')

#django paypal settings
PAYPAL_RECEIVER_EMAIL= 'nachitopsk@gmail.com'
PAYPAL_TEST= True
PAYPAL_BUY_BUTTON_IMAGE= 'https://www.paypalobjects.com/webstatic/es_MX/mktg/logos-buttons/redesign/btn_13.png'

LOGIN_REDIRECT_URL= reverse_lazy('index:index')
LOGOUT_REDIRECT_URL= reverse_lazy('login')

#AUTHENTICATION_BACKENDS = (
#    'django.contrib.auth.backends.ModelBackend',
#    'apps.backend.backends.EmailAuthBackend'
#)

EMAIL_USE_TLS=True
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER='dimercomcarritocompras@gmail.com'
EMAIL_HOST_PASSWORD='carrito123'
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'