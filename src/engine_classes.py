from abc import ABC, abstractmethod
import requests


class Engine(ABC):

    @abstractmethod
    def get_request(self, *args, **kwargs):
        pass

    @staticmethod
    def get_connector(self):
        """Return instance of class Connector"""
        pass


class HH(Engine):
    """Class for work with HeadHunter"""

    def __init__(self, params: str) -> None:
        self.__vacancies = []
        self.__params = params

    @property
    def vacancies(self):
        return self.__vacancies

    def get_request(self, params: dict) -> None:
        """Return request"""
        url_head_hunter = "https://api.hh.ru/vacancies"
        response = requests.get(url_head_hunter, params=params)
        if response.status_code == 200:
            vacancies = response.json()["items"]
            for vacancy in vacancies:
                self.__vacancies.append((vacancy["name"], vacancy["url"], vacancy["area"]["name"], vacancy["snippet"]))
                   # print(vacancy["name"], vacancy["url"], vacancy["area"]["name"], vacancy["snippet"]) # ,vacancy["salary"]["from"], vacancy["salary"]["to"] доделать проверку на ЗП
        else:
            return "Error:", response.status_code



class SJ(Engine):
    """Class for work with SuperJob """

    def __init__(self, api_key: str, params: dict):
        self.__vacancies = []
        self.__params = params
        self.__api_key = api_key

    @property
    def vacancies(self):
        return self.__vacancies

    def get_request(self, params):
        url_super_job = "https://api.superjob.ru/2.0/vacancies/"
        headers = {'X-Api-App-Id': self.__api_key}
        response = requests.get(url_super_job, headers=headers, params=params)
        if response.status_code == 200:
            vacancies = response.json()["objects"]
            for vacancy in vacancies:
                self.__vacancies.append((vacancy["profession"], vacancy["profession"], vacancy["link"],
                                          vacancy["payment_from"], vacancy["payment_to"], vacancy["town"]["title"]))

        else:
            return "Error:", response.status_code



