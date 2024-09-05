from engine.models import Channel


class ChannelRepository:
    model = Channel

    @classmethod
    def create_channel(cls, **kwargs):
        channel = cls.model.objects.create(kwargs)
        return channel

    def get_channel_by_id(cls, channel_id):
        try:
            return cls.model.objects.get(channel_id=channel_id)
        except cls.model.DoesNotExist:
            return None

    @classmethod
    def get_channel_by_pk(cls, channel_pk):
        try:
            return cls.model.objects.get(pk=channel_pk)
        except cls.model.DoesNotExist:
            return None

    @classmethod
    def delete_channel(cls, channel_id):
        try:
            channel = cls.model.objects.get(channel_id=channel_id)
            channel.delete()
            return True
        except cls.model.DoesNotExist:
            return False

    @classmethod
    def get_channels_user(cls, user):
        return cls.model.objects.filter(user=user).all()
