from celery import shared_task


@shared_task
def insert_data_periodically():
    # extract_some_page(1,10)
    # extract_first_page()
    # print("hi")
    return 