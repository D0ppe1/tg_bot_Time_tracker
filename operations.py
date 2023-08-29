import datetime


class Job:
    """docstring"""
    job_id = None
    date_start = None
    date_end = None


class User:
    """docstring"""
    user_id = None
    chat_id = None
    status = None
    job = None

    def start_work(self):
        start_point = datetime.datetime.now()
        print(f'Погнали: {start_point}')
        return start_point

    def end_work(self):
        end_point = datetime.datetime.now()
        print(f'Фуух,закончили {end_point}')
        return end_point


# def safe():
#
# def load():

doppel = User()
# tgbot = Job(12343, '14:27', '16:30')
# doppel = User(99999, 'private', 'none', 'Tgbot')


# print(tgbot)
print(doppel)
