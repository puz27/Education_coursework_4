class Vacancy:
    # __slots__ = ...

    #def __init__(self, *args):
    def __init__(self, name: str, url: str, description: str, area: str, employer: str, experience: str):
        self.__name = name
        self.__url = url
        self.__description = description
        self.__area = area
        self.__employer = employer
        self.__experience = experience

    def __str__(self):
        return f'Наименование:{self.__name} Ссылка:{self.__url} Описание:{self.__description} ' \
               f'Город:{self.__area} Компания:{self.__employer}'



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
    def __init__(self, name: str, url: str, description: str, area: str, employer: str,
                 requirement: str, salary: str, experience: str):
        super().__init__(name, url, description, area, employer, experience)
        self.__requirement = requirement
        self.__salary = salary


    # def __str__(self):
    #     return f'Наименование:{self.__name} Ссылка:{self.__url} Описание:{self.__description} Город:{self.__town} Компания:{self.__employer} Доп.требования:{self.__requirement} Зарплата: {self.__salary} руб/мес'
    #

class SJVacancy(Vacancy):  # add counter mixin
    """ SuperJob Vacancy """
    def __init__(self, name: str, url: str, description: str, town: str, employer: str,
                 salary_from: str, salary_to: str, experience: str):
        super().__init__(name, url, description, town, employer, experience)
        self.__salary_from = salary_from
        self.__salary_to = salary_to

    def __str__(self):
        return f'SJ: {self.comany_name}, зарплата: {self.salary} руб/мес'


def sorting(vacancies):
    """ Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods) """
    pass


def get_top(vacancies, top_count):
    """ Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """
    pass