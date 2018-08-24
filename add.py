from celery import Celery
from time import sleep

app = Celery('add', broker='pyamqp://guest@localhost//')

@app.task(bind=True)
def add(self, x, y):
    print("Y: %s" % y)
    if y == 3:
        self.retry(countdown=10)
    sleep(2)
    return x + y
