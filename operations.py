import datetime
import uuid
import pickle


class Job:
    """docstring"""

    def __init__(self):
        self.job_id = uuid.uuid4()
        self.date_start = datetime.datetime.now()
        self.date_end = None

    def stop(self):
        self.date_end = datetime.datetime.now()

    def is_active(self) -> bool:
        return not bool(self.date_end)


class User:
    """docstring"""

    def __init__(self, user_id):
        self.user_id = user_id
        self.old_jobs = []
        self.job = None
        self.categories = {}

    def start_work(self):
        self.job = Job()

    def end_work(self):
        if self.job.is_active():
            self.job.stop()
            self.old_jobs.append(self.job)
            self.job = None

    def create_category(self, name):
        if name not in self.categories.keys():
            self.categories[name] = (Category(name, self))

    def remove_category(self, name):
        if name in self.categories.keys():
            self.categories.pop(name)


class Category:
    def __init__(self, name: str, author: User):
        """
        Creating instance of Category.
        :param name: Name of Category.
        :param author: User who creates a Category.
        """
        self.name = name
        self.author = author


class Data:
    users = {}

    @staticmethod
    def save():
        """
        Func so save data with pickle
        :param data: dict
        :return:
        """
        try:
            with open('data.pickle', 'wb') as f:
                pickle.dump(Data.users, f)
        except:
            print('Ошибка при сохранении данных')

    @staticmethod
    def load():
        """
        Func so load data with pickle
        :return: data{} or empty{}
        """
        try:
            with open('data.pickle', 'rb') as f:
                data = pickle.load(f)
        except:
            print('Ошибка при загрузке данных')
        # isinstance проверяет чтобы "data" была "dict",т.е. загружаемый файл был словарем
        if isinstance(data, dict):
            Data.users = data
        else:
            Data.users = {}
