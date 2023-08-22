# import time

class Job:
    """1234"""
    def __init__(self,job_id, date_start, date_end):
        self.job_id = job_id
        self.date_start = date_start
        self.date_end = date_end

class User:
    """1234"""
    def __init__(self,user_id, chat_id, status, job):
        self.user_id = user_id
        self.chat_id = chat_id
        self.status = status
        self.job = job

    def start_work(self):

    def end_work(self):



tgbot = Job(12343, '14:27', '16:30')
doppel = User(99999, 231235, 'pause', 'Tgbot')

print(tgbot)
print(doppel)
