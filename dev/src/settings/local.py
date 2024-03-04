from .base import *
from decouple import config, Config, RepositoryEnv
from os.path import join
config = Config(RepositoryEnv(join(BASE_DIR, '.env')))


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

