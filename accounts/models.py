from enum import unique
from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser
# from crypt.
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    phone = models.CharField(max_length=10, null=True, blank=False)
    
    USERNAME_FIELD="email"
    REQUIRED_FIELDS = ["username"]
    class Meta:
        db_table="user_account"


class EmailVerificationCode(models.Model):
    uuid = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    email = models.EmailField(null=False, blank=False)
    code = models.CharField(null=False, blank=False, max_length=20)
    
    class Meta:
        db_table="email_verification_code"

 
 
