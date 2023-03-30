import requests


def requests_params_hh(name_vacancie: str, one_page_count: int = 3, all_page_count: int = 10):
    params = {
        "text": name_vacancie,
        "per_page": one_page_count,
        "page": all_page_count,

    }
    return params


# def get_vacancies_hh(params: dict):
#     """
#     При указании параметров пагинации (page, per_page) работает ограничение: глубина возвращаемых результатов не может быть больше 2000.
#     Например, возможен запрос per_page=10&page=199 (выдача с 1991 по 2000 вакансию),
#     но запрос с per_page=10&page=200 вернёт ошибку (выдача с 2001 по 2010 вакансию)
#     :param params:
#     :return:
#     """
#     url_head_hunter = "https://api.hh.ru/vacancies"
#     response = requests.get(url_head_hunter, params=params)
#     final_information = []
#     if response.status_code == 200:
#         vacancies = response.json()["items"]
#         for vacancy in vacancies:
#             final_information.append((vacancy["name"], vacancy["url"], vacancy["area"]["name"], vacancy["snippet"]))
#         return final_information
#             #print(vacancy["name"], vacancy["url"], vacancy["area"]["name"], vacancy["snippet"]) # ,vacancy["salary"]["from"], vacancy["salary"]["to"] доделать проверку на ЗП
#
#     else:
#         return "Error:", response.status_code


def requests_params_sj(name_vacancie: str, one_page_count: int = 3, all_page_count: int = 3):
    params = {"keywords": name_vacancie,
              "count": one_page_count,
              "page": all_page_count
              }
    return params


# def get_vacancies_sj(api_key: str, params: dict):
#     """
#     Прежде чем начать использовать API, необходимо зарегистрироваться и получить токен для работы,
#     более подробная инструкция описана по ссылке описания документации в разделе Getting started
#     :param api_key:
#     :param params:
#     :return:
#     """
#     url_super_job = "https://api.superjob.ru/2.0/vacancies/"
#     headers = {'X-Api-App-Id': api_key}
#     response = requests.get(url_super_job, headers=headers, params=params)
#     final_information = []
#     if response.status_code == 200:
#         vacancies = response.json()["objects"]
#         for vacancy in vacancies:
#             final_information.append((vacancy["profession"], vacancy["profession"], vacancy["link"],
#                                       vacancy["payment_from"], vacancy["payment_to"], vacancy["town"]["title"]))
#
#         return final_information
#     else:
#         return "Error:", response.status_code


# request to superjob
superjob_api_key = "v3.r.137436720.8c7f8aba97fa695bc8eb530e248876d05b91ac49.93eb1ab45d1127728b93d412484a5f08ae09f2c8"

# for i in get_vacancies_sj(superjob_api_key, requests_params_sj("python")):
#     print(i)

# for i in get_vacancies_hh(requests_params_hh("python")):
#     print(i)

