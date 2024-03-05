from .base import *
from os.path import join
from decouple import config, Config, RepositoryEnv
config = Config(RepositoryEnv(join(BASE_DIR, '.env')))

ENVIRONMENT = config('ENVIRONMENT', default='production')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = [ 'jobsplus.onrender.com']

CSRF_TRUSTED_ORIGINS = [ 'https://jobsplus.onrender.com' ]

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



POSTGRES_LOCALLY = False
if ENVIRONMENT == 'production' or POSTGRES_LOCALLY == True:
    DATABASES['default'] = dj_database_url.parse(config('DATABASE_URL'))

SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_PRELOAD = True
