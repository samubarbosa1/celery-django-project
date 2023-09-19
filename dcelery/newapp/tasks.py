from celery import shared_task
import time


@shared_task
def tp1():
    time.sleep(3)
    return


@shared_task
def tp2():
    time.sleep(3)
    return


@shared_task
def tp3():
    time.sleep(3)
    return


@shared_task
def tp4():
    time.sleep(3)
    return
