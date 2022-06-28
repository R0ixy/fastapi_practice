from celery import Celery
# from kombu import Queue


# def route_task(name, args, kwargs, options, task=None, **kw):
#     if ":" in name:
#         queue, _ = name.split(":")
#         return {"queue": queue}
#     return {"queue": "celery"}


# class CeleryConfig:
#     CELERY_BROKER_URL: str = "amqp://guest:guest@localhost:5672//"
#     result_backend: str = "rpc://"
#
#     CELERY_TASK_QUEUES: list = (
#         # default queue
#         Queue("celery"),
#         # custom queue
#         Queue("email"),
#     )
#
#     CELERY_TASK_ROUTES = (route_task,)


# def create_celery():
#     celery_app = Celery('tasks',
#                         broker='pyamqp://guest:guest@localhost:5672//',
#                         backend='rpc://',
#                         include=['celery_tasks.email_tasks'])
#     celery_app.config_from_object(CeleryConfig)
#     celery_app.conf.task_queues = (
#         # default queue
#         Queue("celery"),
#         # custom queue
#         Queue("email"),
#     )
#     celery_app.conf.task_routes = (route_task,)
#     celery_app.conf.update(task_track_started=True,
#                            task_serializer='pickle',
#                            result_serializer='pickle',
#                            accept_content=['pickle', 'json'],
#                            result_expires=200,
#                            result_persistent=True,
#                            worker_send_task_events=False,
#                            worker_prefetch_multiplier=1)
#     return celery_app

celery_app = Celery('tasks',
                    broker='amqp://guest:guest@localhost:5672//',
                    backend='rpc://',
                    include=['celery_tasks'])
