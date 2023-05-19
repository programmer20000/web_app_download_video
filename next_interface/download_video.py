import os

from pytube import YouTube
from pytube.exceptions import RegexMatchError
from pywebio.input import (input, TEXT)
from pywebio.output import (toast, put_loading, put_text, put_html)

from .next_interface import next_interface


# todo: This function is for create directory
def create_directory(name_directory: str = ''):
    if not os.path.exists(name_directory):
        os.mkdir(name_directory)


# todo: This function is for downloaded video
def download_video():
    create_directory(name_directory='yours_video')

    try:
        link_video = input(
            placeholder='Please enter link video',
            type=TEXT,
            help_text='Please enter only link video',
            required=True
        )

        video = YouTube(url=link_video)
        with put_loading():
            put_text("Yours video is in the process of downloaded...")
            get_video = video.streams.get_highest_resolution()
            get_video.download('yours_video')
        next_interface()

    except RegexMatchError:
        toast('yours link video is incorrect please check link video')
        download_video()
