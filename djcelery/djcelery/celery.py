
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from decouple import config
from celery.schedules import crontab


# set the default Django settings module for the 'celery' program.
# this is also used in manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djcelery.settings')

app = Celery('djcelery')

app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Dhaka')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
# should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

#celery beat settings
app.conf.beat_schedule={
    'scrape-every-8':{
        'task':'core.tasks.Task_Scrapper',
        'schedule': crontab(hour=13,minute=49),
        #'args':
    }
}


# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# We used CELERY_BROKER_URL in settings.py instead of:
# app.conf.broker_url = ''

# We used CELERY_BEAT_SCHEDULER in settings.py instead of:
# app.conf.beat_scheduler = ''django_celery_beat.schedulers.DatabaseScheduler'

#@app.task(bind=True)
#def Task_Hello(self):

    #print("Hello from Task_Hello!")




#celery -A djcelery worker -l info
#celery -A djcelery beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler