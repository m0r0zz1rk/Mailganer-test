import os
import celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = celery.Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'CheckTimeMailing': {
        'task': 'mail.celery.tasks.CheckTimeOfMailings',
        'schedule': crontab(minute='*/10'),
    },
}