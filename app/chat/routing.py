from django.urls import re_path
from app.chat import consumers

websocket_urlpatterns = [
    re_path(r'ws/app/chat/$', consumers.ChatConsumer.as_asgi()),
]
