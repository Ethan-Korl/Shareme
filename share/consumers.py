import json
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
import json

class ShareConsumer(WebsocketConsumer):
    def connect(self):
        self.share_channel_id = self.scope['url_route']['kwargs']['share_channel_id']
        self.room_group_name = f'share_{self.share_channel_id}'
        # self.room_group_name = "shre"
        print(self.share_channel_id)
        # channel = ShareChannel.objects.create(share_channel_id=self.share_channel_id)
        # channel.save()
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        # text_data_json = json.loads(text_data)
        # message = text_data_json['message']
        # username = text_data_json['username']

        # async_to_sync(self.channel_layer.group_send)(
        #     self.room_group_name,
        #     {
        #         'type': 'chat_message',
        #         'message': message,
        #         'username': username
        #     }
        # )
        pass

    def share_file(self, event):
        file_size = event['file_size']
        file_url = event['file_url']
        file_name = event['file_name']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'file_size': file_size,
            'file_url': file_url,
            'file_name': file_name
            }))
