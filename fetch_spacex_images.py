import argparse

import requests

from download_image import download_image


def get_spacex_launch_image_links(launch_id='5eb87d47ffd86e000604b38a'):
    response = requests.get(
        'https://api.spacexdata.com/v5/launches/{0}'.format(launch_id)
    )
    response.raise_for_status()
    return response.json().get('links').get('flickr').get('original')


def fetch_spacex_last_launch(launch_id):
    for image_number, image_link in enumerate(
        get_spacex_launch_image_links(launch_id)
    ):
        download_image(
            image_link,
            'images',
            'spacex_{0}.jpg'.format(image_number)
        )


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-lid' '-launch_id', default='latest', required=False)
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    parsed_launch_id = args.launch_id
    fetch_spacex_last_launch(parsed_launch_id)


if __name__ == '__main__':
    main()
