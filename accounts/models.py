from enum import unique
from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    user_id = models.UUIDField(default=uuid4, primary_key=True)
    username = models.CharField(unique=True, max_length=20)
    email = models.EmailField(unique=True, null=False, blank=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        db_table = "user_account"


class OneTimePassword(models.Model):
    otp_id = models.UUIDField(default=uuid4, unique=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    otp = models.CharField(null=False, blank=False, max_length=20)

    class Meta:
        db_table = "one_time_password"


class EmailVerificationCode(models.Model):
    uuid = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    email = models.EmailField(null=False, blank=False)
    code = models.CharField(null=False, blank=False, max_length=20)

    class Meta:
        db_table = "email_verification_code"
