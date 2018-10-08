import time

from celery import Celery

app = Celery('tasks', broker='amqp://localhost//', backend='db+sqlite:///celery_db.db')

@app.task
def reverse(s):
    time.sleep(10)
    return s[::-1]