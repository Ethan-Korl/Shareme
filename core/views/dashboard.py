from core.views.base import *
from uuid import uuid4


@login_required()
def dashboard(request: HttpRequest):
    channel_repo = ChannelRepository
    channels = channel_repo.get_channels_user(user=request.user)
    context = {"user": request.user, "channels": channels}
    return render(request, "dashboard.html", context)


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


#     request.headers["HX-Target"] = ""

#     channel_layer = get_channel_layer()

#     async_to_sync(channel_layer.group_send)(
#         f'update_channels',
#         # 'shre',
#         {
#             'type': 'share_file',
#         }
#     )
#     return
