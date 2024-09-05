from core.views.base import *
from uuid import uuid4


@login_required()
def dashboard(request: HttpRequest):
    channel_repo = ChannelRepository
    channels = channel_repo.get_channels_user(user=request.user)
    context = {"user": request.user, "channels": channels}
    return render(request, "dashboard.html", context)


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
