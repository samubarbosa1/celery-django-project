from celery import shared_task
import time


@shared_task
def tp1(queue="celery"):
    time.sleep(20)
    return


@shared_task
def tp2(queue="celery:1"):
    time.sleep(20)
    return


@shared_task
def tp3(queue="celery:2"):
    time.sleep(20)
    return


@shared_task
def tp4(queue="celery:3"):
    time.sleep(20)
    return
