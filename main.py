from src.engine_classes import *
from src.utils import *
from src.jobs_classes import Vacancy

x = HH(requests_params_hh("python"))
x.get_request(requests_params_hh("python"))
print(x.vacancies)
for i in x.vacancies:
    print(i)
    temp = HHVacancy(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
    print(temp.__dict__)


y = SJ(superjob_api_key, requests_params_sj("python"))
print(y.get_request(requests_params_sj("python")))
print(y.vacancies)
for i in y.vacancies:
    print("----------")
    temp = SJVacancy(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
    print(temp.__dict__)




