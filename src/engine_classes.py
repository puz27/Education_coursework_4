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

    def __init__(self) -> None:
        self.__vacancies = []

    @property
    def vacancies(self):
        return self.__vacancies

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

                    # данные по experience тянем через этот запрос

                    # id = vacancy["id"]
                    # url_id_request = "https://api.hh.ru/vacancies/" + id
                    # vacancy_id_response = requests.get(url_id_request)

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

                    # получаем всю информацию по запросу

                    self.__vacancies.append({"name": vacancy["name"],
                                             "url": vacancy["url"],
                                             "responsibility": vacancy["snippet"]["responsibility"],
                                             "town": vacancy["area"]["name"],
                                             "employer": vacancy["employer"]["name"],
                                             "requirement": vacancy["snippet"]["requirement"],
                                             "salary_from": str(salary_from),
                                             "salary_to": str(salary_to),
                                             #"experience": vacancy_id_response.json()["experience"]["id"]
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
        self.__api_key = api_key
        #количество результатов на странице

    @property
    def vacancies(self):
        return self.__vacancies

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
                    self.__vacancies.append({"name": vacancy["profession"],
                                             "url": vacancy["link"],
                                             "responsibility": vacancy["candidat"],
                                             "town": vacancy["town"]["title"],
                                             "employer": vacancy["firm_name"],
                                             "requirement": vacancy["work"],
                                             "salary_from": str(vacancy["payment_from"]),
                                             "salary_to": str(vacancy["payment_to"]),
                                             #"experience": vacancy["experience"]["id"]
                                             })

            else:
                return "Error:", response.status_code

            response_page = response.json()["more"]
            page_number += 1
