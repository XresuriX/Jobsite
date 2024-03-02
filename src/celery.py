# celery.py

from __future__ import absolute_import, unicode_literals
import os
import os
import sys

from celery import Celery
import django
from celery.schedules import crontab
from django.conf import settings
from ..jobs.tasks import fetch_data # Make sure the import is correct
from django.conf import settings


# Create a Celery instance and configure it using the Django settings.
app = Celery('src')
app.config_from_object('django.conf:settings', namespace='CELERY')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings.local')
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
django.setup()
from django.conf import settings
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.tasks.register(call_custom_command_task) 

enable_utc = True
"""app.conf.beat_schedule = {
    'task-1': {
        'task': 'jobs.tasks.call_custom_command_task',
        'schedule': crontab(hour='20', minute='0'),
        'args': ('software', '2', 'today'),
    },
    'task-2': {
        'task': 'jobs.tasks.call_custom_command_task',
        'schedule': crontab(hour="20", minute="10"),
        'args': ('', '2', "today"),
    },
    'task-3': {
        'task': 'jobs.tasks.call_custom_command_task',
        'schedule': crontab(hour="20", minute="15"),
        'args': ('logistics', '2', "today"),
    },
    'task-4': {
        'task': 'jobs.tasks.call_custom_command_task',
        'schedule': crontab(hour="20", minute="20"),
        'args': ('business', '2', "today"),
    },
}
"""