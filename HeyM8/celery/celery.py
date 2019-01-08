from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HeyM8.settings')

app = Celery('HeyM8')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

#NOTES

#1) Gather dayetrics, weekmetrics, monthmetrics

#2) every 4 hours delete users and who havn't confirmed email for more than 2 days(and their statistic info)

#3) every 3 hours check users who must be unbanned

#4) every 3 hours check users and communities for breaking (complaint.banning.py)
