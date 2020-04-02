from celery import Celery

REDIS_URL = 'redis://localhost:6379/0'

REDIS_BACKEND_URL = 'redis://localhost:6379/1'


app = Celery('tasks', broker=REDIS_URL, backend=REDIS_BACKEND_URL)




