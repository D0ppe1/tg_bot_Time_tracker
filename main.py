import telebot
import os
from telebot import types
from operations import*

bot = telebot.TeleBot(os.getenv('TOKEN'))


@bot.message_handler(commands=['start'])
def greetings(message):
    bot.send_message(message.chat.id, "Добро пожаловать {0.first_name}!\nЯ - <b>{1.first_name}</b>,"
                                      " бот созданный для отслеживания твоего прогресса."
                     .format(message.from_user, bot.get_me()), parse_mode='html')


@bot.message_handler(content_types=['text'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton(text='Начать отсчёт')
    if message.text == 'Начать отсчёт':
        bot.send_message(message.chat.id, f'Отсчет времени начался:  {doppel.start_work()}\nУдачи 😉')
    btn2 = types.KeyboardButton(text='Поставить на паузу')
    if message.text == 'Поставить на паузу':
        bot.send_message(message.chat.id, 'в разработке Поставить на паузу ')
    btn3 = types.KeyboardButton(text='Продолжить')
    if message.text == 'Продолжить':
        bot.send_message(message.chat.id, 'в разработке Продолжить')
    btn4 = types.KeyboardButton(text='Закончить отсчёт')
    if message.text == 'Закончить отсчёт':
        bot.send_message(message.chat.id, f'Отсчёт времени закончиося:  {doppel.end_work()}\nТы сегодня молодец!😇 ')
    btn5 = types.KeyboardButton(text='Посмотреть количество часов')
    if message.text == 'Посмотреть количество часов':
        bot.send_message(message.chat.id, 'в разработке Посмотреть количество часов')


    keyboard.add(btn1, btn2, btn3, btn4, btn5)
    # bot.send_message(message.chat.id, '1', reply_markup=keyboard)

    # bot.send_message(message.chat.id, message.text)


bot.polling(non_stop=True)
