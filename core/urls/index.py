from django.urls import path
from core.views import *

MAIN_INDEX_URLS = [path("", welcome, name="index")]
