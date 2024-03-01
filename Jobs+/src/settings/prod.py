from .base import *
from decouple import config, Config, RepositoryEnv
from os.path import join
config = Config(RepositoryEnv(join(BASE_DIR, '.env')))

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("api_db"),
        "USER": config("user"),
        "PASSWORD": config('db_pwd'),
        "HOST": config("host"),
        "PORT": config("port"),
        'TEST': {
            'NAME': 'testdb',},
    }  
}

SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_PRELOAD = True
