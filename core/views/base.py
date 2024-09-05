from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpRequest
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from core.models import Channel, channels
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from asgiref.sync import async_to_sync
from core.repository import ChannelRepository
