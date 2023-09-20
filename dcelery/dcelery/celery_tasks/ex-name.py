from dcelery.celery import app


@app.task(queue="celery")
def my_task():
    return
