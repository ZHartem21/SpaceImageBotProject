import telegram

bot = telegram.Bot(token='5787268580:AAESSaptJN5KJ3KQXQ8r9ziVCeqLvov8X7g')

bot.send_photo(
    chat_id='@SpacePicturesProject',
    photo=open('images/epic_0.png', 'rb')
)
