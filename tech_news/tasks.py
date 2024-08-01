from celery import shared_task
from report.webscrapper import extract_first_page

@shared_task
def extract_first_page_task():
    extract_first_page()
    

