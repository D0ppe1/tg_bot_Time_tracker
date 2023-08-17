import telebot
import os

bot = telebot.TeleBot(os.getenv('TOKEN'))


@bot.message_handler(content_types=['text'])
def echoo(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(non_stop=True)
