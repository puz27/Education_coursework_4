from abc import ABC, abstractmethod
import requests
from src.jobs_classes import *

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

    def get_request(self, params: dict) -> None or str:
        """Return request"""
        url_head_hunter = "https://api.hh.ru/vacancies"
        response = requests.get(url_head_hunter, params=params)
        if response.status_code == 200:
            vacancies = response.json()["items"]
            for vacancy in vacancies:

                id = vacancy["id"]
                url_id_request = "https://api.hh.ru/vacancies/" + id
                vacancy_id_response = requests.get(url_id_request)

                # self.__vacancies.append((vacancy["name"], vacancy["url"], vacancy["snippet"]["responsibility"],
                #                          vacancy["area"], vacancy["employer"], vacancy["snippet"]["requirement"],
                #                          vacancy["salary"], vacancy_id_response.json()["experience"]))

                self.__vacancies.append({"name": vacancy["name"],
                                         "url": vacancy["url"],
                                         "responsibility": vacancy["snippet"]["responsibility"],
                                         "area": vacancy["area"],
                                         "employer": vacancy["employer"],
                                         "requirement": vacancy["snippet"]["requirement"],
                                         "salary": vacancy["salary"],
                                         "experience": vacancy_id_response.json()["experience"]
                                         })
        else:
            return "Error:", response.status_code



class SJ(Engine):
    """Class for work with SuperJob """

    def __init__(self, api_key: str, params: dict) -> None:
        self.__vacancies = []
        self.__params = params
        self.__api_key = api_key

    @property
    def vacancies(self):
        return self.__vacancies

    def get_request(self, params: dict) -> None or str:
        url_super_job = "https://api.superjob.ru/2.0/vacancies/"
        headers = {'X-Api-App-Id': self.__api_key}
        response = requests.get(url_super_job, headers=headers, params=params)
        if response.status_code == 200:
            vacancies = response.json()["objects"]
            for vacancy in vacancies:
                # self.__vacancies.append((vacancy["profession"], vacancy["link"], vacancy["candidat"],
                # vacancy["town"],vacancy["work"], vacancy["payment_from"],
                #                          vacancy["payment_to"], vacancy["experience"]))
                self.__vacancies.append({"profession": vacancy["profession"],
                                      "link": vacancy["link"],
                                       "candidat": vacancy["candidat"],
                                       "town": vacancy["town"],
                                       "work": vacancy["work"],
                                       "payment_from": vacancy["payment_from"],
                                       "payment_to": vacancy["payment_to"],
                                       "experience": vacancy["experience"]
                                      })


        else:
            return "Error:", response.status_code

