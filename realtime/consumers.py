import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from todo_list.models import OnlineUser

class TaskConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        self.group_name = 'tasks_group'

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

        if self.user.is_authenticated:
            await self.add_online_user(self.user, self.channel_name)
            # Сповіщаємо всіх, що зайшов новий користувач
            await self.channel_layer.group_send(self.group_name, {
                'type': 'user_status',
                'action': 'joined',
                'username': self.user.username
            })

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

        if self.user.is_authenticated:
            await self.remove_online_user(self.user)
            # Сповіщаємо всіх, що користувач вийшов
            await self.channel_layer.group_send(self.group_name, {
                'type': 'user_status',
                'action': 'left',
                'username': self.user.username
            })

    # Обробка оновлень завдань (від API)
    async def task_update(self, event):
        await self.send(text_data=json.dumps({
            'type': 'task',
            'action': event['action'],
            'task': event['task']
        }))

    # Обробка статусів користувачів (вхід/вихід)
    async def user_status(self, event):
        await self.send(text_data=json.dumps({
            'type': 'user_status',
            'action': event['action'],
            'username': event['username']
        }))

    @database_sync_to_async
    def add_online_user(self, user, channel_name):
        OnlineUser.objects.update_or_create(user=user, defaults={'channel_name': channel_name})

    @database_sync_to_async
    def remove_online_user(self, user):
        OnlineUser.objects.filter(user=user).delete()