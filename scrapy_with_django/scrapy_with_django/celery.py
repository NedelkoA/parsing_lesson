from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scrapy_with_django.settings')

app = Celery('scrapy_with_django', broker='redis://localhost:6379/0')

# app.config_from_object('django.conf:settings')
#
# # Load task modules from all registered Django app configs.
app.autodiscover_tasks(settings.INSTALLED_APPS)
