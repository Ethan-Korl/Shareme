from engine.views.base import *
from uuid import uuid4


@require_http_methods(["DELETE"])
def delete_channel(request: HttpRequest, id):
    channel_repo = ChannelRepository
    result = channel_repo.delete_channel(id)
    if result:
        return
    else:
        return ""


@login_required()
@require_http_methods(["POST"])
def create_channel(request: HttpRequest):
    channel_repo = ChannelRepository

    channel_name = request.POST.get("channel_name")

    channel = channel_repo.create_channel(
        channel_name=channel_name,
        user=request.user,
    )


@require_http_methods(["POST"])
def regenerate_channel_id(request: HttpRequest):
    channel_repo = ChannelRepository

    pk = request.POST.get("channel_pk")

    channel = channel_repo.get_channel_by_pk(channel_pk=pk)
    channel.channel_id = uuid4()
    channel.save()
    return
