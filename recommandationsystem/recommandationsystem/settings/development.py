from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'CONN_HEALTH_CHECKS': 'False',
        'CONN_MAX_AGE': 0,
        'DISABLE_SERVER_SIDE_CURSORS': 'False',
        # 'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': env('DEV_DB_HOST'),
        'NAME': env('DEV_DB_NAME'),
        'PASSWORD': env('DEV_DB_PASSWORD'),
        'PORT': env('DEV_DB_PORT'),
        'USER': env('DEV_DB_USER')
    }
}