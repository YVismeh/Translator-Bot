import telebot
from googletrans import Translator
import os

API_TOKEN = os.environ.get("API_TOKEN")

bot = telebot.TeleBot(API_TOKEN)
translator = Translator()



@bot.message_handler(func=lambda message: True)
def welcome_message(message):
   translated_text = translator.translate(message.text, src="en", dest="fa")
   print (translated_text)
   bot.reply_to(message, translated_text.text)



bot.infinity_polling()