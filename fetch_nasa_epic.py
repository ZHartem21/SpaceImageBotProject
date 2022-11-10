import argparse
import os

import requests
from dotenv import load_dotenv

from download_image import download_image


def get_epic_links(access_token, number_of_images):
    response = requests.get(
        'https://api.nasa.gov/EPIC/api/natural/images',
        params={'api_key': access_token}
    )
    response.raise_for_status()
    epic_link_template = \
        'https://api.nasa.gov/EPIC/archive/natural/{0}/{1}/{2}/png/{3}.png'
    epic_links = []
    for epic_number, epic in enumerate(response.json()):
        if not epic_number < int(number_of_images):
            continue
        year, month, day = epic['date'][:-9].split('-')
        link = epic_link_template.format(
            year,
            month,
            day,
            epic['image']
        )
        epic_links.append(link)
    return epic_links


def fetch_nasa_epic(access_token, number_of_images):
    enumerated_links = enumerate(
        get_epic_links(access_token, number_of_images)
    )
    for image_number, image_link in enumerated_links:
        download_image(
            image_link,
            'images',
            'epic_{0}.png'.format(image_number),
            params={'api_key': access_token}
        )


def create_parser():
    parser = argparse.ArgumentParser(description='Fetch NASA EPIC images')
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
    fetch_nasa_epic(nasa_access_token, parsed_number_of_images)


if __name__ == '__main__':
    main()
