import telebot
from googletrans import Translator
import os

API_TOKEN = os.environ.get("API_TOKEN")

bot = telebot.TeleBot(API_TOKEN)
translator = Translator()



# this code translate your message to persen

@bot.message_handler(func=lambda message: True)
def translate_message(message):
    #detection = translator.detect(message.text)
    #print("Language code:", detection.lang)
    translated_text = translator.translate(message.text, dest="fa", src="auto")
    print(f"{translated_text.origin} ({translated_text.src}) --> {translated_text.text} ({translated_text.dest})")
    bot.reply_to(message, f"{translated_text.origin} ({translated_text.src})\n\n ترجمه\n\n{translated_text.text} ({translated_text.dest})")



# this code translate your message to japenese

# @bot.message_handler(regexp="ja")
# def to_ja_message(message):
#     translated_text = translator.translate(message.text, dest="ja", src="fa")
#     print(translated_text)
#     bot.reply_to(message, translated_text.text)



# this code translate your message to french

# @bot.message_handler(regexp="fr")
# def to_fr_message(message):
#     translated_text = translator.translate(message.text, dest="fr", src="fa")
#     print(translated_text)
#     bot.reply_to(message, translated_text.text)



bot.infinity_polling()