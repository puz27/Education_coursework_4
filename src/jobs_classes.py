class Vacancy:
    # __slots__ = ...

    def __init__(self, *args):
        self.__name = args[0]
        self.__url = args[1]
        self.__responsibility = args[2]
        self.__town = args[3]
        self.__employer = args[4]
        self.__requirement = args[5]
        self.__salary_from = args[6]
        self.__salary_to = args[7]
        self.__expierence = args[7]


    def __str__(self):
        return f'Наименование:{self.__name} Ссылка:{self.__url} Описание:{self.__responsibility}' \
               f'Город:{self.__town} Компания:{self.__employer}'

    # def __repr__(self):
    #     return f"Название вакансии: {self.__name}\nСсылка на вакансию: {self.__url}\n"



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
    # def __init__(self, name: str, url: str, description: str, area: str, employer: str,
    #              requirement: str, salary: str, experience: str):

    def __init__(self, *args):
        super().__init__(*args)


    # def __str__(self):
    #     return f'Наименование:{self.__name} Ссылка:{self.__url} Описание:{self.__description} Город:{self.__town} Компания:{self.__employer} Доп.требования:{self.__requirement} Зарплата: {self.__salary} руб/мес'
    #

class SJVacancy(Vacancy):  # add counter mixin
    """ SuperJob Vacancy """

    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        return f'SJ: {self.__employer}, зарплата: {self.__salary_from} руб/мес'


def sorting(vacancies):
    """ Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods) """
    pass


def get_top(vacancies, top_count):
    """ Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """
    pass