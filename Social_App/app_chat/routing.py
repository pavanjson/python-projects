from django.urls import path
from .consumers import RoomChatConsumer

websocket_urlpatterns=[
    path("ws/chat-group/<str:room>/", RoomChatConsumer.as_asgi(), name="public_chat"),
]
