import telebot
from googletrans import Translator
import os

API_TOKEN = os.environ.get("API_TOKEN")

bot = telebot.TeleBot(API_TOKEN)
translator = Translator()



@bot.message_handler(regexp="ja")
def to_ja_message(message):
    translated_text = translator.translate(message.text, src="fa", dest="ja")
    print(translated_text)
    bot.reply_to(message, translated_text.text)


@bot.message_handler(regexp="fr")
def to_fr_message(message):
    translated_text = translator.translate(message.text, src="fa", dest="fr")
    print(translated_text)
    bot.reply_to(message, translated_text.text)


# @bot.message_handler(func=lambda message: True)
# def welcome_message(message):
#    translated_text = translator.translate(message.text, src="en", dest="fa")
#    print (translated_text)
#    bot.reply_to(message, translated_text.text)



bot.infinity_polling()