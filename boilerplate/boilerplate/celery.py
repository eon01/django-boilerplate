from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

if (os.environ['DJANGO_ENV'] == "prod"):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "boilerplate.settings.prod")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "boilerplate.settings.dev")
    
app = Celery('boilerplate')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)