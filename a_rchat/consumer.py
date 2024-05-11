from channels.generic.websocket import WebsocketConsumer

class ChatroomConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()