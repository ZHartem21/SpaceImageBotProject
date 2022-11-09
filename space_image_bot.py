import argparse
import os
import random
import time

import telegram
from dotenv import load_dotenv


def post_shuffled_images_in_folder(directory='images', timer='14400'):
    telegram_bot_token = os.environ['TELEGRAM_TOKEN']
    bot = telegram.Bot(token=telegram_bot_token)
    original_folder, folders, files = list(os.walk(directory))[0]
    print(files)
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
    parser = argparse.ArgumentParser()
    parser.add_argument('-t' '-timer', default='14400', required=False)
    parser.add_argument('-f' '-folder', default='images', required=False)
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    parsed_timer = args.timer
    parsed_folder = args.folder
    load_dotenv('access_tokens.env')
    post_shuffled_images_in_folder(parsed_folder, parsed_timer)


if __name__ == '__main__':
    main()
