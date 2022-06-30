from pathlib import Path

from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

from core.config import settings


conf = ConnectionConfig(
    MAIL_USERNAME=settings.SMTP_LOGIN,
    MAIL_PASSWORD=settings.SMTP_PASSWORD,
    MAIL_FROM="fitter@email.com",
    MAIL_PORT=settings.SMTP_PORT,
    MAIL_SERVER=settings.SMTP_SERVER,
    MAIL_FROM_NAME="FastApi Email Service",
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
    TEMPLATE_FOLDER=Path(__file__).parent.parent/'email_templates',
)

fm = FastMail(conf)


async def send_email_task(email, token):
    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=[email],
        template_body={
            'domain': '127.0.0.1:3000',
            'token': token
        },
        subtype="html"
    )
    await fm.send_message(message, template_name="confirm_email.html")
    return "Email sent"

