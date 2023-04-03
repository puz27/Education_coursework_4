class Vacancy:
    # __slots__ = ...

    def __init__(self, args):
        self.__name = args["name"]
        self.__url = args["url"]
        self.__responsibility = args["responsibility"]
        self.__town = args["town"]
        self.__employer = args["employer"]
        self.__requirement = args["requirement"]
        self.__salary_from = args["salary_from"]
        self.__salary_to = args["salary_to"]
        self.limit = 10

    @property
    def salary_to(self):
        return self.__salary_to

    @property
    def salary_from(self):
        return self.__salary_from

    def __str__(self):
        return f'Наименование: {self.__name}\nСсылка: {self.__url}\nОписание: {self.__responsibility}\n'\
               f'Город: {self.__town}\nКомпания: {self.__employer}\nТребования: {self.__requirement}\n'\
               f'ЗП от: {self.__salary_from}\nЗП до: {self.__salary_to}'

class CountMixin:

    @property
    def get_count_of_vacancy(self):
        """
        Вернуть количество вакансий от текущего сервиса.
        Получать количество необходимо динамически из файла.
        """
        pass


class HHVacancy(Vacancy):  # add counter mixin
    """ HeadHunter Vacancy """

    def __str__(self):
        return f"Данные с HeadHunter\n{super().__str__()}\n"


class SJVacancy(Vacancy):  # add counter mixin
    """ SuperJob Vacancy """

    def __lt__(self, other):
        return int(self.salary_to) < int(other.salary_to)

    def __le__(self, other):
        return int(self.salary_to) <= int(other.salary_to)

    def __str__(self):
        return f"Данные с SuperJob\n{super().__str__()}\n"

