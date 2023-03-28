from src.engine_classes import *
from src.utils import *

x = HH(requests_params_hh("python"))
print(x.get_request(requests_params_hh("python")))
print(x.vacancies)


y = SJ(superjob_api_key, requests_params_sj("python"))
print(y.get_request(requests_params_sj("python")))
print(y.vacancies)

