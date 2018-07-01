from celery import Celery
import time

celery = Celery(broker='amqp://jack:111111@47.96.237.51:15672/')

@celery.task
def send_sms():
    time.sleep(5)
    print('sms')