from django.urls import path
from engine.views import *

CHANNEL_URLS = [
    path("update-channel-id", regenerate_channel_id, name="update-channel-id"),
]
