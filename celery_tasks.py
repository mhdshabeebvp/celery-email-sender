from celery import Celery
from celery.utils.log import get_task_logger
import smtplib
from email.mime.text import MIMEText

logger = get_task_logger(__name__)

app = Celery(
    "celery_tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)

# Configuration for Celery Beat
app.conf.beat_schedule = {
    "send-email-every-20-seconds": {
        "task": "celery_tasks.send_email_task",
        "schedule": 20.0,
    },
}


@app.task
def send_email_task():
    sender_email = "*******@gmail.com"
    receiver_email = "*******@gmail.com"
    message = "hello, shabeeb your celery project success!"

    msg = MIMEText(message)
    msg["Subject"] = "Celery Project Success"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        # Setup the SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            # Login to your Gmail account
            server.login(sender_email, "sender_gmail_password")
            # Send email
            server.sendmail(sender_email, receiver_email, msg.as_string())
            logger.info("Email sent successfully")
    except smtplib.SMTPException as e:
        logger.error("Error while sending email: %s", str(e))
