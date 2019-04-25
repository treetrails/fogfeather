"""
Django settings for fogfeather project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import dj_database_url
from django.conf.global_settings import DATETIME_INPUT_FORMATS

# ISO 8601 datetime format to accept html5 datetime input values
DATETIME_INPUT_FORMATS += ["%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M"]

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zcej%w=e5lym(@y)01q6c&*5@eobs%pzgtens$!9l332$(by_7'

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
    'django_saml2_auth',
    'rest_framework',
    'crispy_forms',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'fogfeather.urls'

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

WSGI_APPLICATION = 'fogfeather.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# SAML2
SAML2_AUTH = {
    # Metadata is required, choose either remote url or local file path
    'METADATA_AUTO_CONF_URL': '[The auto(dynamic) metadata configuration URL of SAML2]',
    'METADATA_LOCAL_FILE_PATH': '[The metadata configuration file path]',

    # # Optional settings below
    # 'DEFAULT_NEXT_URL': '/admin',  # Custom target redirect URL after the user get logged in. Default to /admin if not set. This setting will be overwritten if you have parameter ?next= specificed in the login URL.
    # 'CREATE_USER': 'TRUE', # Create a new Django user when a new user logs in. Defaults to True.
    # 'NEW_USER_PROFILE': {
    #     'USER_GROUPS': [],  # The default group name when a new user logs in
    #     'ACTIVE_STATUS': True,  # The default active status for new users
    #     'STAFF_STATUS': True,  # The staff status for new users
    #     'SUPERUSER_STATUS': False,  # The superuser status for new users
    # },
    # 'ATTRIBUTES_MAP': {  # Change Email/UserName/FirstName/LastName to corresponding SAML2 userprofile attributes.
    #     'email': 'Email',
    #     'username': 'UserName',
    #     'first_name': 'FirstName',
    #     'last_name': 'LastName',
    # },
    # 'TRIGGER': {
    #     'CREATE_USER': 'path.to.your.new.user.hook.method',
    #     'BEFORE_LOGIN': 'path.to.your.login.hook.method',
    # },
    # 'ASSERTION_URL': 'https://mysite.com', # Custom URL to validate incoming SAML requests against
    # 'ENTITY_ID': 'https://mysite.com/saml2_auth/acs/', # Populates the Issuer element in authn request
    # 'NAME_ID_FORMAT': FormatString, # Sets the Format property of authn NameIDPolicy element
    # 'USE_JWT': False, # Set this to True if you are running a Single Page Application (SPA) with Django Rest Framework (DRF), and are using JWT authentication to authorize client users
    # 'FRONTEND_URL': 'https://myfrontendclient.com', # Redirect URL for the client if you are using JWT auth with DRF. See explanation below
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Extra places for collectstatic to find static files.
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
#
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'