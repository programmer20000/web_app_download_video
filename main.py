import os

import pywebio
from pywebio import start_server
from pywebio.output import (clear, put_image)

from next_interface import (download_video)


class Interface:
    def __init__(self):
        # todo: here we setup  window with title and theme properties
        pywebio.config(title='Download Video', theme='dark')

    def run(self):
        clear()
        logo_path = os.path.join('image', 'logo.jpg')
        put_image(open(file=logo_path, mode='rb').read())
        download_video()


if __name__ == '__main__':
    interface = Interface()
    start_server(interface.run, port=8000, debug=True)
