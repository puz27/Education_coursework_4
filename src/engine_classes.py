from abc import ABC, abstractmethod
from src.utils import format_text
import requests


class Engine(ABC):

    @abstractmethod
    def get_request(self, *args, **kwargs):
        pass


class HH(Engine):
    """Class for work with HeadHunter"""

    def __init__(self) -> None:
        self.__vacancies = []
        self.__config = [{"last request": "Последний запрос был к HEAD HUNTER"}]

    @property
    def vacancies(self):
        return self.__vacancies

    @property
    def config(self):
        return self.__config

    def get_request(self, keywords: str) -> None or str:
        """Return request"""
        print("Делаем запрос с HEAD HUNTER")
        url_head_hunter = "https://api.hh.ru/vacancies"
        page_number = 0
        all_pages = 1

        #while page_number < all_pages:
        while page_number < 2:

            params = {
                "text": keywords,
                "per_page": 100,
                "page": page_number,
                        }

            response = requests.get(url_head_hunter, params=params)
            if response.status_code == 200:

                vacancies = response.json()["items"]
                for vacancy in vacancies:

                    # Обработка данных по заработной плате
                    if vacancy["salary"] is not None:
                        salary_from = vacancy["salary"]["from"]
                        if salary_from is None:
                            salary_from = 0
                        salary_to = vacancy["salary"]["to"]
                        if salary_to is None:
                            salary_to = 0
                    else:
                        salary_from = 0
                        salary_to = 0

                    # Обработка формата для поля responsibility/requirement
                    convert_responsibility = format_text(vacancy["snippet"]["responsibility"])
                    convert_requirement = format_text(vacancy["snippet"]["requirement"])

                    # получаем всю информацию по запросу
                    self.__vacancies.append({"name": vacancy["name"],
                                             "url": vacancy["url"],
                                             "responsibility": convert_responsibility,
                                             "town": vacancy["area"]["name"],
                                             "employer": vacancy["employer"]["name"],
                                             "requirement": convert_requirement,
                                             "salary_from": str(salary_from),
                                             "salary_to": str(salary_to),
                                             })
            else:
                return "Error:", response.status_code

            #all_pages = response.json()["pages"]
            all_pages = 1
            page_number += 1


class SJ(Engine):
    """Class for work with SuperJob """

    def __init__(self, api_key: str) -> None:
        self.__vacancies = []
        self.__config = [{"last request": "Последний запрос был к SUPER JOB"}]
        self.__api_key = api_key

    @property
    def vacancies(self):
        return self.__vacancies

    @property
    def config(self):
        return self.__config

    def get_request(self, keywords: str) -> None or str:
        print("Делаем запрос с SUPER JOB")
        url_super_job = "https://api.superjob.ru/2.0/vacancies/"
        headers = {'X-Api-App-Id': self.__api_key}
        page_number = 1
        response_page = True

        while response_page:

            params = {"keywords": keywords,
                      "count": 100,
                      "page": page_number,
                      }

            response = requests.get(url_super_job, headers=headers, params=params)
            if response.status_code == 200:
                vacancies = response.json()["objects"]

                for vacancy in vacancies:
                    # Обработка формата для поля responsibility/requirement
                    convert_responsibility = format_text(vacancy["candidat"])
                    convert_requirement = format_text(vacancy["work"])

                    self.__vacancies.append({"name": vacancy["profession"],
                                             "url": vacancy["link"],
                                             "responsibility": convert_responsibility,
                                             "town": vacancy["town"]["title"],
                                             "employer": vacancy["firm_name"],
                                             "requirement": convert_requirement,
                                             "salary_from": str(vacancy["payment_from"]),
                                             "salary_to": str(vacancy["payment_to"])
                                             })

            else:
                return "Error:", response.status_code

            response_page = response.json()["more"]
            page_number += 1
