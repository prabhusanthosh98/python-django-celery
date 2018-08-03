from celery import shared_task
import time


@shared_task
def execute_long_work(model):
    print('Starting long execution')

    time.sleep(5)
    print('almost there')

    time.sleep(5)


    print('Done')

