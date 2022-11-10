import os

import requests


def download_image(url, directory, filename, params={}):
    response = requests.get(url, params=params)
    response.raise_for_status()
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, filename), 'wb') as file:
        file.write(response.content)
