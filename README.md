# Space Image Telegram Bot

This tool allows to automatically download space images from various sources, and then set up a bot that automatically posts image folder in the telegram channel.

## How to install

### Requirements 

Python3 should already be installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Environment variables

Two tokens are required for using the tool:
1. Nasa API token
2. Telegram bot API token

After gaining access to both of the tokens, you must create a new file called **access_tokens.env** in the project folder, and store two tokens inside of it as:
1. `NASA_TOKEN`
2. `TELEGRAM_TOKEN`

## How to use

To dowload images you can use one of the three scripts:
1. `fetch_spacex_images.py` - downloads pictures from a spacex rocket launch. Has an argument `-lid` that allows to specify launch id. By default, downloads photos from the latest launch.
2. `fetch_nasa_epic.py` - downloads pictures from NASA EPIC API. Has an argument `-n` that allows to specify required number of images to download.
3. `fetch_nasa_apod.py` - downloads astronomy picture of a day from NASA. Also has an argument `-n`.

To start the bot you must launch the *space_image_bot* in terminal. There are two arguments:
`-f` - Image folder, default is 'images'
`-t` - Posting timer in seconds, default is 4 hours(14400 seconds)
```
python space_image_bot.py -f=images -t=14400
```

## Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).