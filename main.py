import telebot
import os
from telebot import types
from operations import User

bot = telebot.TeleBot(os.getenv('TOKEN'))

data = {}


def registr_user(user_id):
    '''
    Check is in data.keys() an user_id and if not func create key:val
    :param user_id: int
    :return:
    '''
    print(data)
    if user_id not in data.keys():
        data[user_id] = User(user_id=user_id)


def get_keyboard():
    '''
    Crate keyboard
    :return: keyboard
    '''
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton(text='Начать отсчёт')
    btn2 = types.KeyboardButton(text='Поставить на паузу')
    btn3 = types.KeyboardButton(text='Продолжить')
    btn4 = types.KeyboardButton(text='Закончить отсчёт')
    btn5 = types.KeyboardButton(text='Посмотреть количество часов')
    keyboard.add(btn1, btn2, btn3, btn4, btn5)
    return keyboard
@bot.message_handler(commands=['start'])
def greetings(message):
    registr_user(user_id=message.from_user.id)
    greeting_text = f"Добро пожаловать {message.from_user.first_name}!\nЯ - <b>{bot.get_me().first_name}</b>," \
                    " бот созданный для отслеживания твоего прогресса."
    bot.send_message(chat_id=message.chat.id, text=greeting_text, parse_mode='html',reply_markup=get_keyboard())


@bot.message_handler(content_types=['text'])
def start(message):
    registr_user(user_id=message.from_user.id)
    text = None
    if message.text == 'Начать отсчёт':
        text = '///'
    elif message.text == 'Поставить на паузу':
        text = 'в разработке Поставить на паузу '
    elif message.text == 'Продолжить':
        text = 'в разработке Продолжить'
    elif message.text == 'Закончить отсчёт':
        text = '///'
    elif message.text == 'Посмотреть количество часов':
        text = 'в разработке Посмотреть количество часов'
    if text:
        bot.send_message(chat_id=message.chat.id, text=text, parse_mode='html',reply_markup=get_keyboard())

    # bot.send_message(message.chat.id, message.text)


bot.polling(non_stop=True)
