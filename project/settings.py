import os
from configparser import RawConfigParser

PROJECT_NAME = 'nash_dom'
PROJECT_VERSION = '1.0.0'
AUTHOR = 'Maksim <kmg.xammi.1@gmail.com>'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PRODUCTION_DIR = f'/opt/{PROJECT_NAME}'

production_config = os.path.join('/etc', PROJECT_NAME, f'{PROJECT_NAME}.conf')
development_config = os.path.join(BASE_DIR, 'local', f'{PROJECT_NAME}.conf')
config_path = production_config if os.path.exists(production_config) else development_config

config = RawConfigParser()
config.read(config_path)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.get('common', 'SECRET_KEY', fallback='!SECRET_KEY!')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.getboolean('common', 'DEBUG', fallback=False)

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bot',
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

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'project.wsgi.application'


# TODO: logging
# TODO: telegram secret


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'local', 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'null': {
            'class': 'logging.NullHandler',
        },
    },
    'loggers': {},
}

LOG_FILE = config.get('logging', 'LOG_FILE', fallback='/var/log/nash_dom/bot.log')

if not os.path.exists(LOG_FILE) and os.path.exists(os.path.dirname(LOG_FILE)):
    with open(LOG_FILE, 'w') as log_file:
        log_file.write('\n')

if os.path.exists(LOG_FILE) and os.access(LOG_FILE, os.W_OK):
    LOGGING['handlers']['logfile'] = {
        'class': 'logging.handlers.WatchedFileHandler',
        'filename': LOG_FILE,
        'formatter': 'verbose'
    }
    LOGGING['loggers']['django'] = {
        'handlers': ['logfile', 'console'] if DEBUG else ['logfile'],
        'level': 'INFO' if DEBUG else 'ERROR',
        'propagate': False,
    }
    LOGGING['loggers'][PROJECT_NAME] = {
        'handlers': ['logfile', 'console'] if DEBUG else ['logfile'],
        'level': 'INFO',
        'propagate': False
    }
