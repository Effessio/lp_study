from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lp_study.settings')


app = Celery('lp_study',
             broker='amqp://',
             backend='amqp://',
             include=['lp_study.tasks'])

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


if __name__ == '__main__':
    app.start()