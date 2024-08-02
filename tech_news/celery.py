import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tech_news.settings')
app = Celery("tech_news")

app.config_from_object("django.conf:settings", namespace="CELERY")

@app.task
def add_nums():
    return

app.autodiscover_tasks()    

# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Schedule to call extract_first_page every hour
#     sender.add_periodic_task(crontab(minute=0, hour='*/1'), extract_first_page_task.s(), name='extract_first_page every hour')

# @app.task
# def extract_first_page_task():
#     from .webscrapper import extract_first_page
#     extract_first_page()
