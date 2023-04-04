
from src.engine_classes import *
from src.utils import user_questions, user_search, user_search_answers
from src.connector import Connector
from src.jobs_classes import Vacancy
import json
import os
user_answer = ""
user_question = False

# основное меню пользователя
while True:
    print(*user_questions[0])
    user_answer = input()

    # Завершить обработку
    if user_answer == user_questions[0]["5.Завершить обработку"]:
        break

    # Запросить данные с сайта HEAD HUNTER
    if user_answer == user_questions[0][" 1.Запросить данные с сайта HEAD HUNTER\n"]:
        head_hunter = HH()
        head_hunter.get_request("python")
        head_hunter_connector = Connector("information.json")
        head_hunter_connector.insert(head_hunter.vacancies)

    # Запросить данные с сайта SUPER JOB
    elif user_answer == user_questions[0]["2.Запросить данные с сайта SUPER JOB\n"]:
        sj_api_key = "v3.r.137436720.8c7f8aba97fa695bc8eb530e248876d05b91ac49.93eb1ab45d1127728b93d412484a5f08ae09f2c8"
        super_job = SJ(sj_api_key)
        super_job.get_request("python")
        super_job_connector = Connector("information.json")
        super_job_connector.insert(super_job.vacancies)

    # Работа с файлом
    elif user_answer == user_questions[0]["3.Работа с файлом\n"]:

        head_hunter_connector = Connector("information.json")
        # Валидация файла
        if head_hunter_connector.validate() is True:

            while True:
                print(*user_questions[1])
                user_answer = input()
                if user_answer == user_questions[1]["3.Выйти в команды верхнего меню\n"]:
                    break
                # Выбор данных их файла
                elif user_answer == user_questions[1][" 1.Выбор данных их файла\n"]:
                    head_hunter_connector.validate()

                    # Поле для поиска
                    while True:
                        print("Выберите поле для поиска.\n")
                        print(*user_search)
                        user_answer_key = input()

                        if user_answer_key in str((1, 2, 3, 4, 5, 6, 7, 8)):
                            break
                        else:
                            print("! Введите корректную команду !\n")

                    # Значение поля поиска
                    user_answer_value = input("Введите значение. Регистр важен.\n")
                    search_filter = {user_search_answers[user_answer_key]:  user_answer_value}
                    print(head_hunter_connector.select(search_filter))
                    input("Для продолжения нажмите Enter...")

                # Удаление данных их файла
                elif user_answer == user_questions[1]["2.Удаление данных их файла\n"]:
                    head_hunter_connector.validate()

                    # Поле для удаления вакансии
                    while True:
                        print("Выберите поле для операции удаления вакансии.\n")
                        print(*user_search)
                        user_answer_key = input()

                        if user_answer_key in str((1, 2, 3, 4, 5, 6, 7, 8)):
                            break
                        else:
                            print("! Введите корректную команду !\n")

                    # Значение поля для удаления вакансии
                    user_answer_value = input("Введите значение для удаления. Регистр важен.\n")
                    search_filter = {user_search_answers[user_answer_key]: user_answer_value}
                    print(f"Было удалено:{head_hunter_connector.delete(search_filter)} вакансий.")
                    input("Удаление выполнено. Для продолжения нажмите Enter...")

                else:
                    print(*user_questions[3])

    # Работа с вакансиями
    elif user_answer == user_questions[0]["4.Работа с вакансиями\n"]:
        while True:
            print(*user_questions[2])
            user_answer = input()
            if user_answer == user_questions[2]["4.Выйти в команды верхнего меню\n"]:
                break
            if user_answer == user_questions[2][" 1.Вывести произвольное количество вакансий из файла\n"]:
                user_question = True
                print("Вывести произвольное количество вакансий из файла")
            if user_answer == user_questions[2]["2.Вывести самые высокооплачиваемые вакансии\n"]:
                user_question = True
                print("Вывести самые высокооплачиваемые вакансии")
            if user_answer == user_questions[2]["4.Выйти в команды верхнего меню\n"]:
                user_question = True
                print("Глубокий поиск по вакансиям")
            else:
                print("! Введите корректную команду !\n")

    else:
        print(*user_questions[3])

















