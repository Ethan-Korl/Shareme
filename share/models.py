from django.db import models
from uuid import uuid4
# Create your models here.

from django.db import models

class ShareChannel(models.Model):
    share_channel_id = models.CharField(unique=True, max_length=50)


class File(models.Model):
    file = models.FileField()
    shared_at = models.DateTimeField(auto_now_add=True) 