class Vacancy:
    # __slots__ = ...

    #def __init__(self, *args, **kwargs):
    def __init__(self, name: str = None, url: str = None, description: str = None,
                 salary: float = None, employer: str = None, town: str = None):
        self.__name = name
        self.__url = url
        self.__description = description
        self.salary = salary
        self.employer = employer
        self.town = town


    # def __str__(self):
    #     pass

    def __repr__(self):
        return f"Название вакансии: {self.__name}\nСсылка на вакансию: {self.__url}\n"



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
        return f'HH: {self.comany_name}, зарплата: {self.salary} руб/мес'



class SJVacancy(Vacancy):  # add counter mixin
    """ SuperJob Vacancy """

    def __str__(self):
        return f'SJ: {self.comany_name}, зарплата: {self.salary} руб/мес'


def sorting(vacancies):
    """ Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods) """
    pass


def get_top(vacancies, top_count):
    """ Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """
    pass