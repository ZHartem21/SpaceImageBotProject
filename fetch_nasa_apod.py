import argparse
import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv

from download_image import download_image


def scan_file_extension(url):
    return os.path.splitext(urlparse(url).path)[1]


def get_nasa_apod_links(access_token, number_of_images=1):
    response = requests.get(
        'https://api.nasa.gov/planetary/apod',
        params={'api_key': access_token, 'count': number_of_images}
    )
    response.raise_for_status()
    apod_links = []
    for apod in response.json():
        if scan_file_extension(apod.get('url')):
            apod_links.append(apod.get('url'))
    return apod_links


def fetch_nasa_apod(access_token, number_of_images):
    enumarated_links = enumerate(
        get_nasa_apod_links(access_token, number_of_images)
    )
    for image_number, image_link in enumarated_links:
        download_image(
            image_link,
            'images',
            'nasa_{0}{1}'.format(
                image_number,
                scan_file_extension(image_link)
            )
        )


def create_parser():
    parser = argparse.ArgumentParser(description='Fetch NASA APOD images')
    parser.add_argument(
        '-n',
        '-number_of_images',
        default=1,
        required=False,
        help='Select number of images to download (default: 1)'
        )
    return parser


def main():
    load_dotenv('access_tokens.env')
    nasa_access_token = os.environ['NASA_TOKEN']
    parser = create_parser()
    args = parser.parse_args()
    parsed_number_of_images = args.n
    fetch_nasa_apod(nasa_access_token, parsed_number_of_images)


if __name__ == '__main__':
    main()
