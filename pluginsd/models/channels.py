from django.db import models
from uuid import uuid4
# Create your models here.


class Channel(models.Model):
    user = models.IntegerField()
    channel_name = models.CharField(max_length=60, null=True, blank=True)
    channel_id = models.UUIDField(default=uuid4, unique=True)
