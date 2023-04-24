import os


class Channel:
    """Класс для ютуб-канала"""
    API_KEY = os.getenv('API_KEY_YOUTube')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(self.print_info)
