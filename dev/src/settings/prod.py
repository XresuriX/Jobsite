from .base import *
import os
from decouple import config, Config, RepositoryEnv
config = Config(RepositoryEnv(join(BASE_DIR, '.env')))

ENVIRONMENT = config('ENVIRONMENT', default='production')

SECRET_KEY = os.environ.get('SECRET_KEY')


DEBUG = False

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

ROOT_URLCONF = "dev.src.urls"

STATIC_URL = '/static/'

# This production code might break development mode, so we check whether we're in DEBUG mode
if not DEBUG:
    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
    # and renames the files with unique names for each version to support long-term caching
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

POSTGRES_LOCALLY = False
if ENVIRONMENT == 'production' or POSTGRES_LOCALLY == True:
    DATABASES['default'] = dj_database_url.parse(config('DATABASE_URL'))

SECURE_HSTS_SECONDS = 3153600  # 1 year
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_PRELOAD = True
