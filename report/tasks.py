from celery import shared_task
from .webscrapper import extract_first_page

@shared_task
def extract_first_page_task():
    print("######## Running periodic task ##########")
    # return
    extract_first_page()