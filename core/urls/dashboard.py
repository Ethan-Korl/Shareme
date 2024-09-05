from django.urls import path
from core.views import *

DASHBOARD_URLS = [
    path("dashboard/", dashboard, name="dashboard"),
]
