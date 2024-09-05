from rest_framework import serializers


class FileSerilizer(serializers.Serializer):
    file = serializers.FileField()
    share_channel_id = serializers.CharField()
