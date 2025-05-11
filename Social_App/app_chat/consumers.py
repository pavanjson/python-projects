from django.shortcuts import get_object_or_404, HttpResponse
import json
from asgiref.sync import async_to_sync
from django.template.loader import render_to_string
from channels.generic.websocket import WebsocketConsumer

# --- Import from own Apps ---------
from .models import GroupMessage, ChatGroup


# ===== ROOM or GROUP CHAT CONSUMER =====
class RoomChatConsumer(WebsocketConsumer):
    async def connect(self):
        
        return self.accept()
    
    def disconnect(self, code):
        pass
    
    def receive(self, text_data):
        pass

