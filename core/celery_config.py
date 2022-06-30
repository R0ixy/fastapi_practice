from celery import Celery

from core.config import settings

celery_app = Celery('tasks',
                    broker=f'amqp://{settings.CELERY_USER}:{settings.CELERY_PASSWORD}@{settings.CELERY_HOST}:5672//',
                    backend='rpc://',
                    include=['utils.celery_tasks'])
