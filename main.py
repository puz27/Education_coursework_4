from src.engine_classes import *
from src.utils import *
from src.connector import Connector
from src.jobs_classes import Vacancy
import json
import os

#
# x = HH()
# x.get_request("python")
# z = 0
# eee = x.vacancies
# for i in x.vacancies:
#     z += 1
# print(z)
# con = Connector("information.json")
# con.insert(eee)


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

# y = SJ(superjob_api_key)
# y.get_request("python")
# eee = y.vacancies
s = Connector("information.json")
d = s.select({"*": "*"})
for i in d:
    print(i)
    sj =SJ(i)
    print(sj)

#
# con = Connector("information.json")
# con.insert(eee)
#
# temp = HHVacancy(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
# print(temp.__dict__)
