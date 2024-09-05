from django.db import models
from accounts.models import CustomUser
from uuid import uuid4


class ApiKeys(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    key = models.UUIDField(default=uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_blacklisted = models.BooleanField(default=False)
