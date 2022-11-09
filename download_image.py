import os

import requests


def create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)


def download_image(url, directory, filename, params={}):
    response = requests.get(url, params=params)
    response.raise_for_status()
    create_directory(directory)
    with open(os.path.join(directory, filename), 'wb') as file:
        file.write(response.content)
