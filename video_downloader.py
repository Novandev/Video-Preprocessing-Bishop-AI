from pytube import Playlist
from pytube import YouTube


def video_scraper(url_string:str):
    yt = YouTube(url_string)
    yt.streams[0].download()


if __name__ == "__main__":
    video_scraper('https://www.youtube.com/watch?v=WaiNd1wTCt0')