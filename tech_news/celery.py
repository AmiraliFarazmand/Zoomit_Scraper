# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery
# from celery.schedules import crontab

# # set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tech_news.settings')

# app = Celery('tech_news')

# # Using a string here means the worker doesn't have to serialize
# # the configuration object to child processes.
# # - namespace='CELERY' means all celery-related configuration keys
# #   should have a `CELERY_` prefix.
# app.config_from_object('django.conf:settings', namespace='CELERY')

# # Load task modules from all registered Django app configs.
# app.autodiscover_tasks()


# app.conf.beat_schedule = {
#     'extract-first-page-every-hour': {
#         'task': 'app.tasks.extract_first_page_task',
#         'schedule': crontab(minute=0, hour='*/1'),  # Executes every hour
#     },
# }

import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tech_news.settings")
app = Celery("tech_news")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Schedule to call extract_first_page every hour
    sender.add_periodic_task(crontab(minute=0, hour='*/1'), extract_first_page_task.s(), name='extract_first_page every hour')

@app.task
def extract_first_page_task():
    from .webscrapper import extract_first_page
    extract_first_page()
