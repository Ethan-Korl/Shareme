from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from .models import File

# from rest_framework.
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from channels.layers import get_channel_layer
from rest_framework import status
from rest_framework.response import Response
from apis.serializers import FileSerilizer
from asgiref.sync import async_to_sync

# Create your views here.


class ShareFile(CreateAPIView):
    serializer_class = FileSerilizer
    parser_classes = [FormParser, MultiPartParser]

    def post(self, request: HttpRequest, *args, **kwargs):
        current_site = get_current_site(request)
        current_domain = current_site.domain
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            file = serializer.validated_data.get("file")
            share_channel_id = serializer.validated_data.get("share_channel_id")
            print(file)
            print(share_channel_id)
            shared_file = File.objects.create(file=file)
            shared_file.save()
            protocol = "http"
            if request.is_secure():
                protocol = "https"

            file_full_url = f"{protocol}://{current_domain}{shared_file.file.url}"

            channel_layer = get_channel_layer()

            async_to_sync(channel_layer.group_send)(
                f"share_{share_channel_id}",
                # 'shre',
                {
                    "type": "share_file",
                    "file_name": shared_file.file.name,
                    "file_size": shared_file.file.size,
                    "file_url": file_full_url,
                },
            )
            return JsonResponse(data={"message": "File sent", "status": True})
        return JsonResponse(data={"message": "File sent failed", "status": False})
