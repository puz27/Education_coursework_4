from src.engine_classes import *
from src.utils import user_questions, user_search, user_search_answers, user_search_vacancies,user_search_answers_vacancies
from src.connector import Connector
from src.jobs_classes import HHVacancy, SJVacancy

user_answer = ""
user_question = False

# для теста стоит 1 по умолчанию 0
type_of_request = 1


# основное меню пользователя
while True:
    print(*user_questions[0])
    user_answer = input()

    # Завершить обработку
    if user_answer == user_questions[0]["5.Завершить обработку"]:
        break

    # Запросить данные с сайта HEAD HUNTER
    if user_answer == user_questions[0][" 1.Запросить данные с сайта HEAD HUNTER\n"]:
        search_filter = input("Введите слово поиска для вакансии\n").lower()
        head_hunter = HH()
        head_hunter.get_request(search_filter)
        respond = head_hunter.vacancies

        if respond:
            type_of_request = 1
            head_hunter_connector = Connector("information.json")
            head_hunter_connector.insert(head_hunter.vacancies)
        else:
            print("Введен некорректный запрос\n")

    # Запросить данные с сайта SUPER JOB
    elif user_answer == user_questions[0]["2.Запросить данные с сайта SUPER JOB\n"]:
        search_filter = input("Введите слово поиска для вакансии\n")
        sj_api_key = "v3.r.137436720.8c7f8aba97fa695bc8eb530e248876d05b91ac49.93eb1ab45d1127728b93d412484a5f08ae09f2c8"
        super_job = SJ(sj_api_key)
        super_job.get_request(search_filter)
        respond = super_job.vacancies

        if respond:
            type_of_request = 2
            super_job_connector = Connector("information.json")
            super_job_connector.insert(super_job.vacancies)
        else:
            print("Введен некорректный запрос\n")

    # Работа с файлом
    elif user_answer == user_questions[0]["3.Работа с файлом\n"]:

        connector = Connector("information.json")
        # Валидация файла
        if connector.validate() is True:

            while True:
                print(*user_questions[1])
                user_answer = input()
                if user_answer == user_questions[1]["3.Выйти в команды верхнего меню\n"]:
                    break
                # Выбор данных их файла
                elif user_answer == user_questions[1][" 1.Выбор данных их файла\n"]:
                    connector.validate()

                    # Поле для поиска
                    while True:
                        print("Выберите поле для поиска.\n")
                        print(*user_search)
                        user_answer_key = input()

                        if user_answer_key in str((1, 2, 3, 4, 5, 6, 7, 8)):
                            break
                        else:
                            print("! Некорректная команда ввода !\n")

                    # Значение поля поиска
                    user_answer_value = input("Введите значение. Регистр важен.\n")
                    search_filter = {user_search_answers[user_answer_key]:  user_answer_value}
                    print(connector.select(search_filter))
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

        head_hunter_connector = Connector("information.json")
        # Валидация файла
        if head_hunter_connector.validate() is True:

            while True:

                if type_of_request == 1:
                    print("Последний запрос был к сайту HEAD HUNTER")
                if type_of_request == 2:
                    print("Последний запрос был к сайту SUPER JOB")

                print(*user_questions[2])
                user_answer = input()
                if user_answer == user_questions[2]["4.Выйти в команды верхнего меню\n"]:
                    break

                elif user_answer == user_questions[2][" 1.Вывести произвольное количество вакансий из файла\n"]:
                    print("Вывести произвольное количество вакансий из файла")

                # Вывести N самых высокооплачиваемые вакансии
                elif user_answer == user_questions[2]["2.Вывести N самых высокооплачиваемые вакансии\n"]:

                    count_of_vacancies = int(input("Ввести количество вакансий.\n"))

                    # Обработка для HEAD HUNTER
                    if type_of_request == 1:
                        head_hunter_vacancies = HHVacancy
                        connector = Connector("information.json")

                        all_vacancy = connector.select({"*": "*"})
                        sort_dict = []
                        for vacancy in all_vacancy:
                            vacancy_instance = HHVacancy(vacancy)
                            sort_dict.append(vacancy_instance)

                        sort_dict.sort(reverse=True)
                        for vacancy in sort_dict[:count_of_vacancies]:
                            print(vacancy)

                    # Обработка для SUPER JOB
                    if type_of_request == 2:
                        super_job_vacancies = SJVacancy
                        connector = Connector("information.json")

                        all_vacancy = connector.select({"*": "*"})
                        sort_dict = []
                        for vacancy in all_vacancy:
                            vacancy_instance = SJVacancy(vacancy)
                            sort_dict.append(vacancy_instance)

                        sort_dict.sort(reverse=True)
                        for vacancy in sort_dict[:count_of_vacancies]:
                            print(vacancy)







                # Гибкий поиск по вакансиям
                elif user_answer == user_questions[2]["3.Глубокий поиск по вакансиям\n"]:

                    # Запрос на критерии поиска и поиск по этим критериям
                    while True:
                        print("Выбрать поле для поиска.\n")
                        print(*user_search_vacancies)
                        user_answer_key = input("Введите значение для поиска.")

                        if user_answer_key in str((1, 2, 3, 4, 5)):
                            break
                        else:
                            print("! Некорректная команда ввода !\n")

                    user_answer_value = input("Введите значение для поиска. Ищем совпадения. Регистр важен.\n")
                    search_filter = {user_search_answers_vacancies[user_answer_key]: user_answer_value}
                    print(search_filter)

                    # Обработка для HEAD HUNTER
                    if type_of_request == 1:
                        head_hunter_vacancies = HHVacancy
                        connector = Connector("information.json")
                        all_vacancy = connector.select({"*": "*"})

                        if user_answer_key == "1":
                            for vacancy in all_vacancy:
                                vacancy_instance = HHVacancy(vacancy)
                                if user_answer_value in vacancy_instance.name:
                                    print(vacancy_instance)

                        elif user_answer_key == "2":
                            for vacancy in all_vacancy:
                                vacancy_instance = HHVacancy(vacancy)
                                if user_answer_value in vacancy_instance.responsibility:
                                    print(vacancy_instance)

                        elif user_answer_key == "3":
                            for vacancy in all_vacancy:
                                vacancy_instance = HHVacancy(vacancy)
                                if user_answer_value in vacancy_instance.town:
                                    print(vacancy_instance)

                        elif user_answer_key == "4":
                            for vacancy in all_vacancy:
                                vacancy_instance = HHVacancy(vacancy)
                                if user_answer_value in vacancy_instance.employer:
                                    print(vacancy_instance)

                        elif user_answer_key == "5":
                            for vacancy in all_vacancy:
                                vacancy_instance = HHVacancy(vacancy)
                                if user_answer_value in str(vacancy_instance.requirement):
                                    print(vacancy_instance)






                else:
                    print(*user_questions[3])

    else:
        print(*user_questions[3])

















