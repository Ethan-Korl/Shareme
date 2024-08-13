from django.http import HttpRequest
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from core.models import Channel
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from asgiref.sync import async_to_sync
# Create your views here.

@login_required()
def dashboard(request: HttpRequest):
    channels = Channel.objects.filter(user=request.user).all()
    context = {
        "user":request.user,
        "channels":channels
    }
    return render(request, "dashboard.html", context)


def delete_channel(request: HttpRequest):
    pass


@login_required()
@require_http_methods(['POST'])
def create_channel(request: HttpRequest):
    request.headers["HX-Target"] = ""

    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        f'update_channels', 
        # 'shre',
        {
            'type': 'share_file',
        }
    )
    return 




