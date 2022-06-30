from celery import shared_task


@shared_task(autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 5},
             name='tasks:send_email_task')
async def do_something(email, token):
    """Example celery task"""
    ...
