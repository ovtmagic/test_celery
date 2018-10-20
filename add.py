from celery import Celery
from celery.exceptions import MaxRetriesExceededError
from time import sleep

app = Celery('add', broker='pyamqp://guest@localhost//')

@app.task(bind=True)
def add(self, x, y):
    print("Y: %s" % y)
    if y == 3:
        try:
            self.retry(countdown=2)
        except MaxRetriesExceededError as e:
            print("Exception: %s" % e)
            return False
    sleep(10)
    return x + y

@app.task(bind=True)
def add2(self, x, y):
    print("Y: %s" % y)
    if y == 3:
            self.retry(countdown=2)
    sleep(10)
    return x + y


@app.task
def subtask(z):
    print("SUBTAREA: %s" % z)
    return 0



@app.task(bind=True)
def add_noretry(self, x, y):
    print("No retry X,Y: %s,%s" % (x,y))
    subtask.apply_async(args=[x+y])
    return x + y
