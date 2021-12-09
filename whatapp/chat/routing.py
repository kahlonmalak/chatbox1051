from django.urls import path
from .import consumers

websocket_urlpatterns = [
    path(r'^ws/notification/broadcast/', consumers.ChatConsumer.as_asgi()),
]