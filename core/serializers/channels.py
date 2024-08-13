from rest_framework.serializers import ModelSerializer
from core.models import Channel

class ChannelSerializer(ModelSerializer):
    class Meta:
        model = Channel