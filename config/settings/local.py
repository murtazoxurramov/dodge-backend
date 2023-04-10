from decouple import config

DEBUG = config('debug')

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.psycopg2',
        'NAME': config('database_name'),
        'USERNAME': config('database_username'),
        'PASSWORD': config('database_password'),
        'HOST': config('database_hostname'),
        'PORT': '',
    }
}
