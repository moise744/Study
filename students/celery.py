import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'students.settings')

app = Celery('students')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
