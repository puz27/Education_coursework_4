import requests

#req = requests.get('https://api.hh.ru/employers', auth=('user', 'pass'))
# print(req)
# print(req.headers)
# print(req.content)
# Authorization: Bearer ACCESS_TOKEN
# par = {'per_page': '10', 'page': 10}
# #requests.get(self.url, params=par)
# r = requests.get('https://api.hh.ru/employers', params=par)
# print(r.content)
# import requests


# request to hh
def get_vacancies_hh():
    url_head_hunter = "https://api.hh.ru/vacancies"
    params = {
        "text": "python",
        "per_page": 5
    }
    response = requests.get(url_head_hunter, params=params)
    if response.status_code == 200:
        vacancies = response.json()["items"]
        for vacancy in vacancies:
             print(vacancy["name"], vacancy["url"], vacancy["area"]["name"], vacancy["salary"]["from"], vacancy["salary"]["to"])
    else:
        print("Error:", response.status_code)


# request to superjob
superjob_api_key = "v3.r.137436720.8c7f8aba97fa695bc8eb530e248876d05b91ac49.93eb1ab45d1127728b93d412484a5f08ae09f2c8"

def get_vacancies_sj(api_key):
    url_super_job = "https://api.superjob.ru/2.0/vacancies/"
    headers = {'X-Api-App-Id': api_key}
    params = {"keywords": "Python, python"}

    response = requests.get(url_super_job, headers=headers, params=params)
    if response.status_code == 200:
        vacancies = response.json()["objects"]
        for vacancy in vacancies:
            print(vacancy["profession"], vacancy["town"]["title"])
    else:
        print("Error:", response.status_code)

get_vacancies_sj(superjob_api_key)
get_vacancies_hh()
