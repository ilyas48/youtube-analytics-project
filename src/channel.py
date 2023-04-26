import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    API_KEY = os.getenv('API_KEY_YOUTube')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel_json_info = ''
        self.get_channel_json_info()

    def get_channel_json_info(self):
        """Метод получения информации о канале в формате json"""
        with build('youtube', 'v3', developerKey=Channel.API_KEY) as channel_info:
            channel = channel_info.channels().list(id=self.channel_id, part='snippet,statistics').execute()
            self.channel_json_info = json.dumps(channel, indent=2, ensure_ascii=False)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(self.channel_json_info)
