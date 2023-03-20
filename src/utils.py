import requests

url_head_hunter = "https://api.hh.ru/vacancies"

params = {
    "text": "python",
    "per_page": 5
}

# response = requests.get(url_head_hunter, params=params)
# if response.status_code == 200:
#     vacancies = response.json()["items"]
#     for vacancy in vacancies:
#          print(vacancy["name"], vacancy["url"], vacancy["area"]["name"], vacancy["salary"]["from"], vacancy["salary"]["to"])
# else:
#     print("Error:", response.status_code)


url_super_job = "https://api.superjob.ru/2.0/vacancies/"
params2 = {
    "profession": "Старший специалист по тестированию",
    "keys": "python",
    "count": 10,
    "page": 1

}

response = requests.get(url_super_job, params=params2)
print(response.json())