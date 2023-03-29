from src.engine_classes import *
from src.utils import *
from src.jobs_classes import Vacancy

# x = HH(requests_params_hh("python"))
# x.get_request(requests_params_hh("python"))
# print(x.vacancies)
# for i in x.vacancies:
#     print(i)
#     for z in i:
#         print(z)



y = SJ(superjob_api_key, requests_params_sj("python"))
print(y.get_request(requests_params_sj("python")))
print(y.vacancies)
for i in y.vacancies:
    temp = Vacancy(i[0], i[1])
    print(temp)




