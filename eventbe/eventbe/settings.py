import os
from pathlib import Path
from typing import List

import environ

env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, 'secret_key'),
    ALLOWED_HOSTS=(list, ['*']),
    DEFAULT_USER_ACTIVITY=(bool, True),
    MAIL_SENDER=(str, 'v0v.voron2005@yandex.ru'),
)

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(BASE_DIR / '.env')

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

DEFAULT_USER_ACTIVITY = env('DEFAULT_USER_ACTIVITY')

MAIL_SENDER = env('MAIL_SENDER')

ALLOWED_HOSTS: List[str] = env('ALLOWED_HOSTS')
INTERNAL_IPS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third party
    'debug_toolbar',
    'sorl.thumbnail',
    'django_cleanup.apps.CleanupConfig',
    'django_filters',
    # Ours
    'about.apps.AboutConfig',
    'core.apps.CoreConfig',
    'events.apps.EventsConfig',
    'feedback.apps.FeedbackConfig',
    'home.apps.HomeConfig',
    'map.apps.MapConfig',
    'users.apps.UsersConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'eventbe.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'eventbe.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth'
        '.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth'
        '.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth'
        '.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth'
        '.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static_dev',
]

LOGIN_REDIRECT_URL = '/auth/profile/'

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'

EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'
