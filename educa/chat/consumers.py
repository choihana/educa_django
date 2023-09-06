import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        #연결 수락
        self.accept()

    def disconnect(self, close_code):
        #소켓이 닫힐 때 호출되며, 특별한 작업을 수행하지 않도록 pass
        pass

    #websocket에서 메시지 수신
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        #메시지를 websocket으로 전송
        self.send(text_data=json.dumps({'message':message}))