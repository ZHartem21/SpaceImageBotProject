import argparse
import os
import random
import time

import telegram
from dotenv import load_dotenv


def post_specified_image(bot, image, directory='images'):
    print(image)
    bot.send_photo(
        chat_id='@SpacePicturesProject',
        photo=open(os.path.join(directory, image), 'rb')
    )


def post_shuffled_images_in_folder(bot, directory='images', timer='14400'):
    original_folder, folders, files = list(os.walk(directory))[0]
    while True:
        for file in files:
            bot.send_photo(
                chat_id='@SpacePicturesProject',
                photo=open(os.path.join('images', file), 'rb')
            )
            time.sleep(3)
        random.shuffle(files)
        time.sleep(timer)


def create_parser():
    parser = argparse.ArgumentParser(description='Upload images to telegram')
    parser.add_argument(
        '-t',
        '-timer',
        default='14400',
        required=False,
        help='Timer in seconds (Default: 14400'
    )
    parser.add_argument(
        '-f',
        '-folder',
        default='images',
        required=False,
        help='Image folder (Default: images'
    )
    parser.add_argument(
        '-i',
        '-image',
        required=False,
        help='Specific image to upload'
    )
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    parsed_timer = args.t
    parsed_folder = args.f
    parsed_image = args.i
    load_dotenv('access_tokens.env')
    telegram_bot_token = os.environ['TELEGRAM_TOKEN']
    telegram_bot = telegram.Bot(token=telegram_bot_token)
    if parsed_image:
        post_specified_image(telegram_bot, parsed_image)
    else:
        post_shuffled_images_in_folder(
            telegram_bot,
            parsed_folder,
            parsed_timer
        )


if __name__ == '__main__':
    main()
