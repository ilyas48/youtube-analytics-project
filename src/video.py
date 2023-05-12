import json
import os
from googleapiclient.discovery import build


class Video:
    """Класс для ютуб-канала"""
    API_KEY = os.getenv('API_KEY_YOUTube')

    def __init__(self, video_id):
        self.video_id = video_id
        youtube = build('youtube', 'v3', developerKey='AIzaSyC-4j13M0Xk0NnC4w4BVanF64fO5Lv0uUI')
        self.video_response = youtube.videos().list(part='snippet,statistics', id=self.video_id).execute()
        self.title = self.video_response['items'][0]['snippet']['title']
        self.views_count = self.video_response['items'][0]['statistics']['viewCount']
        self.likes_count = self.video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return f'{self.title}'


class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
        youtube = build('youtube', 'v3', developerKey='AIzaSyC-4j13M0Xk0NnC4w4BVanF64fO5Lv0uUI')
        playlist = youtube.playlists().list(id=self.playlist_id, part='snippet').execute()
        self.playlist_name = playlist['items'][0]['snippet']['title']

    def __repr__(self):
        return f'{self.title} ({self.playlist_name}) {self.likes_count}'


