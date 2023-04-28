import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    API_KEY = os.getenv('API_KEY_YOUTube')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel_json_info = self.get_channel_json_info()
        self.title = self.channel_json_info['items'][0]['snippet']['title']
        self.channel_description = self.channel_json_info['items'][0]['snippet']['description']
        self.url = r'https://www.youtube.com/channel/' + self.__channel_id
        self.video_count = self.channel_json_info['items'][0]['statistics']['videoCount']
        self.channel_view_count = self.channel_json_info['items'][0]['statistics']['viewCount']

    def get_channel_json_info(self):
        """Метод получения информации о канале в формате json"""
        youtube = build('youtube', 'v3', developerKey=Channel.API_KEY)
        return youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel_json_info, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        service = build('youtube', 'v3', developerKey=Channel.API_KEY)
        return service

    def to_json(self, filename):
        data = {'title': self.channel_json_info}
        with open(f'{filename}', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

