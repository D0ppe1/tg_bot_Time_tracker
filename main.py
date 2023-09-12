import telebot
import os
# from telebot import types
from operations import User, Data


class App:

    def __init__(self):
        self.bot = telebot.TeleBot(os.getenv('TOKEN'))
        Data.load()
        self.register_handlers()
        self.bot.polling(non_stop=True)

    @staticmethod
    def register_user(user_id):
        """

        :param user_id: int
        :return: None
        """
        print(Data.users)
        # Check is in data.keys() an user_id and if not, func is creat key:val
        if user_id not in Data.users.keys():
            Data.users[user_id] = User(user_id=user_id)
            Data.save()

    @staticmethod
    def get_keyboard():
        """
        Crate keyboard
        :return: keyboard
        """
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = telebot.types.KeyboardButton(text='Начать отсчёт')
        btn2 = telebot.types.KeyboardButton(text='Поставить на паузу')
        btn3 = telebot.types.KeyboardButton(text='Продолжить')
        btn4 = telebot.types.KeyboardButton(text='Закончить отсчёт')
        btn5 = telebot.types.KeyboardButton(text='Посмотреть количество часов')
        keyboard.add(btn1, btn2, btn3, btn4, btn5)
        return keyboard

    def register_handlers(self):
        @self.bot.message_handler(commands=['start'])
        def start_handler(message):
            self.register_user(user_id=message.from_user.id)
            greeting_text = f"Добро пожаловать {message.from_user.first_name}!" \
                            f"\nЯ - <b>{self.bot.get_me().first_name}</b>," \
                            " бот созданный для отслеживания твоего прогресса."
            self.bot.send_message(chat_id=message.chat.id, text=greeting_text, parse_mode='html',
                                  reply_markup=self.get_keyboard())

        @self.bot.message_handler(content_types=['text'])
        def text_handler(message):
            self.register_user(user_id=message.from_user.id)
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
                self.bot.send_message(chat_id=message.chat.id, text=text, parse_mode='html',
                                      reply_markup=self.get_keyboard())

            # bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    app = App()
