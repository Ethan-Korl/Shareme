from django.urls import re_path

# we user re_path due to the limitation we have in normal urls routing
from engine.consumers import websoket_consumer

# fro
websocket_urlpatterns = []
