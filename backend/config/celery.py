from __future__ import absolute_import

import os

from django.conf import settings
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('config', 
             backend='rpc://', 
             broker='pyamqp://myuser:password@localhost:5672/sample_host'
             )


@app.task(bind=True)
def debug_task(self):
    print('REQUEST: {0!r}'.format(self.request))

        