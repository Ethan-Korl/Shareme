from django.urls import path
from core.views import *

DASHBOARD_URLS = [
    path("dashboard/", dashboard, name="dashboard"),
    path("update-channel-id", regenerate_channel_id, name="update-channel-id"),
]
