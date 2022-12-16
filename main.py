from telegram import KeyboardButton,Update
import telegram
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
import json


TOKEN = "5874141721:AAHprnHkQKf7XnaIGSinLI1Y-j8T2Blc_kI"

bot = telegram.Bot(token=TOKEN)

class Quizes_bot:
    def start(update:Update, context:CallbackContext):
        txt = "Salom"
        id = update.message.from_user.id
        url = 'http://127.0.0.1:8000/api/quiz/'
        rq = requests.get(url)
        data_json = rq.json()
        reply_markup = KeyboardButton[data_json['title']]
        updater.bot.sendMessage(txt, id, 'Fanlar ro\'yxati', reply_markup=reply_markup)

updater = Updater(TOKEN)

updater.start_polling()
updater.idle()