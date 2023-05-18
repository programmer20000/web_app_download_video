import os
from shutil import rmtree

from pywebio.output import (toast, put_row, put_button, put_html, put_file)


def download_video_file():
    path_file = os.listdir('../yours_video')[0]
    # todo: we now read password from file
    with open(file=f'yours_video/{path_file}', mode='rb') as file:
        content = file.read()
        put_file(name=path_file, content=content, label='download video')
        toast('Yours video successful downloaded on yours computer')
    rmtree('yours_video', ignore_errors=True)


def refresh_page(func):
    put_html('<h1>This function not  implemented just now</h1>')


def make_buttons():
    put_row([put_button(label='refresh page', onclick=refresh_page), None,
             put_button(label='download video',
                        onclick=download_video_file)],
            size='16% 16px 16%')


def next_interface():
    toast('yours downloaded successful')
    put_html('<h1>Thank you for using our service</h1>')
    make_buttons()
