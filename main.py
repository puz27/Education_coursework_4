from src.engine_classes import *
from src.utils import *
from src.connector import Connector
from src.jobs_classes import Vacancy
import json
import os


# x = HH(requests_params_hh("python"))
# x.get_request(requests_params_hh("python"))
# print(x.vacancies)
# for i in x.vacancies:
#     print(i)
#     temp = HHVacancy(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
#     print(temp.__dict__)
#
# print("__________________________________")
#
# y = SJ(superjob_api_key, requests_params_sj("python"))
# print(y.get_request(requests_params_sj("python")))
# #print(y.vacancies)
# for i in y.vacancies:
#     temp = SJVacancy(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
#
#     print(temp.__dict__)

# y = SJ(superjob_api_key, requests_params_sj("python"))
# y.get_request(requests_params_sj("python"))
# eee = y.vacancies
# print(eee)
#
tes = Connector("information.json")


query = {"link": "https://www.superjob.ru/vakansii/razrabotchik-po-45548247.html"}
tes.delete(query)
print(tes.data_file)

