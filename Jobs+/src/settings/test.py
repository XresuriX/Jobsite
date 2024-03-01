from .base import *
from celery.schedules import crontab
from decouple import config, Config, RepositoryEnv
from os.path import join
config = Config(RepositoryEnv(join(BASE_DIR, '.env')))

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "test",
        "USER": config("user"),
        "PASSWORD": config('db_pwd'),
        "HOST": config("host"),
        "PORT": config("port"),
        "TEST": {
            "NAME": "test",
        },
    }
}

## Celery Configuration
CELERY_BROKER_URL = "pyamqp://guest:guest@localhost:5672//"
CELERY_RESULT_BACKEND = "django-db"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "UTC"

CELERY_BEAT_SCHEDULE = {
    "task-1": {
        "task": "jobs.tasks.call_custom_command_task",
        "schedule": crontab(hour="6", minute="0"),
        "args": ("software", "2", "today"),
    },
    "task-2": {
        "task": "jobs.tasks.call_custom_command_task",
        "schedule": crontab(hour="6", minute="10"),
        "args": ("customer", "2", "today"),
    },
    "task-3": {
        "task": "jobs.tasks.call_custom_command_task",
        "schedule": crontab(hour="22", minute="15"),
        "args": ("logistics", "2", "today"),
    },
    "task-4": {
        "task": "jobs.tasks.call_custom_command_task",
        "schedule": crontab(hour="22", minute="20"),
        "args": ("business", "2", "today"),
    },
}

# Use Django Celery Beat
#INSTALLED_APPS += ["django_celery_beat", "django_celery_results", "request", 'analytical']
#MIDDLEWARE+= ["request.middleware.RequestMiddleware"]

# Celery Results Configuration
CELERY_RESULT_BACKEND = "django-db"

# Celery Cache Configuration
CELERY_CACHE_BACKEND = "django-cache"

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

REQUEST_BASE_URL ='https://www.Jobs+/home/'