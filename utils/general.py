from utils.base import *
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


class Encrypt:
    def __init__(self) -> None:
        self.key = str(settings.SECRET_KEY).encode()
        self.fernet = Fernet(self.key)

    def encrypt(self, otp_code):
        return self.fernet.encrypt(str(otp_code).encode())

    def decryption(self, msg):
        return self.fernet.decrypt(msg).decode()


class SendEmail:
    def __init__(self, user_email, template: str, subject: str, context: dict) -> None:
        self.user_email = user_email
        self.template = template
        self.context = context
        self.render = render_to_string
        email_body = self.render(template, self.context)
        self.email = EmailMessage(
            subject=subject,
            body=email_body,
            from_email=settings.EMAIL_HOST_USER,
            to=[user_email],
        )

    def send_email(self):
        self.email.content_subtype = "html"
        self.email.send(fail_silently=True)
