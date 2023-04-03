from src.engine_classes import *
from src.utils import *
from src.connector import Connector
from src.jobs_classes import Vacancy
import json
import os
user_answer = ""
user_question = False

# основное меню пользователя
while True:
    print("""Выберите действие:
1.Запросить данные с сайта HEAD HUNTER
2.Запросить данные с сайта SUPER JOB   
3.Работа с файлом
4.Работа с вакансиями   
5.Завершить обработку
    """)
    user_answer = input()
    if user_answer == "5":
        break

    # работа с Head Hunter
    if user_answer == "1":
        head_hunter = HH()
        head_hunter.get_request("python")
        head_hunter_connector = Connector("information.json")
        head_hunter_connector.insert(head_hunter.vacancies)


    # работа Super Job
    elif user_answer == "2":
        sj_api_key = "v3.r.137436720.8c7f8aba97fa695bc8eb530e248876d05b91ac49.93eb1ab45d1127728b93d412484a5f08ae09f2c8"
        super_job = SJ(sj_api_key)
        super_job.get_request("python")
        super_job_connector = Connector("information.json")
        super_job_connector.insert(super_job.vacancies)

    # работа с файлом с данными
    elif user_answer == "3":
        head_hunter_connector = Connector("information.json")
        head_hunter_connector.validate()
        while True:
            print("""Выберите действие:
1.Выбор данных их файла
2.Удалить данные из файла
3.Выйти в команды верхнего меню
                  """)
            user_answer = input()
            if user_answer == "3":
                break
            if user_answer == "1":
                user_question = True
                print("Выборка")
            if user_answer == "2":
                user_question = True
                print("Удаление")
            else:
                print("! Введите корректную команду !\n")

     # работа с вакансиями
    elif user_answer == "4":
        while True:
            print("""Выберите действие:
1.Вывести рандомное количество вакансий из файла
2.Вывести самые высокооплачиваемые вакансии
3.Глубокий поиск по вакансиям
4.Выйти в команды верхнего меню
                     """)
            user_answer = input()
            if user_answer == "4":
                break
            if user_answer == "1":
                user_question = True
                print("Вывести рандомное количество вакансий из файла")
            if user_answer == "2":
                user_question = True
                print("Вывести самые высокооплачиваемые вакансии")
            if user_answer == "3":
                user_question = True
                print("Глубокий поиск по вакансиям")
            else:
                print("! Введите корректную команду !\n")

    else:
        print("! Введите корректную команду !\n")






















