
from django.core.mail import send_mail
from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

@shared_task
def send_feedback_email_task(email_subject,email_address, message):
    email_message = EmailMultiAlternatives(email_subject,'',settings.EMAIL_HOST_USER,[email_address])
    email_message.attach_alternative(message, "text/html")
    email_message.send()