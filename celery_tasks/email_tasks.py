from celery import shared_task
from celery.result import AsyncResult


@shared_task(autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 5},
             name='tasks:send_email_task')
def send_email_task():
    ...


def get_task_info(task_id):
    """
    return task info for the given task_id
    """
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return result
