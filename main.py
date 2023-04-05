from src.engine_classes import *
from src.utils import user_questions, user_search, user_search_answers, user_search_vacancies,user_search_answers_vacancies
from src.connector import Connector
from src.jobs_classes import HHVacancy, SJVacancy

user_answer = ""
user_question = False

connector_to_file = Connector("information.json")
connector_to_file_config = Connector("configuration.json")

# основное меню пользователя
while True:
    # Основное меню взаимодействия
    print(*user_questions[0])
    user_answer = input()

    # Завершить обработку
    if user_answer == user_questions[0]["5.Завершить обработку"]:
        break

    # Запросить данные с сайта HEAD HUNTER
    if user_answer == user_questions[0][" 1.Запросить данные с сайта HEAD HUNTER\n"]:
        search_filter = input("Введите слово поиска для вакансии\n")

        # Создаем экземпляр для работы с HEAD HUNTER и делаем запрос
        head_hunter = HH()

        head_hunter.get_request(search_filter)
        respond = head_hunter.vacancies

        # Если данные получили, записываем в файл
        if respond:
            connector_to_file_config.insert(head_hunter.config)
            connector_to_file.insert(head_hunter.vacancies)

        else:
            print("Нет данных по запросу.\n")

    # Запросить данные с сайта SUPER JOB
    elif user_answer == user_questions[0]["2.Запросить данные с сайта SUPER JOB\n"]:
        search_filter = input("Введите слово поиска для вакансии\n")

        # Создаем экземпляр для работы с SUPER JOB и делаем запрос
        sj_api_key = "v3.r.137436720.8c7f8aba97fa695bc8eb530e248876d05b91ac49.93eb1ab45d1127728b93d412484a5f08ae09f2c8"
        super_job = SJ(sj_api_key)
        super_job.get_request(search_filter)
        respond = super_job.vacancies

        # Если данные получили, записываем в файл
        if respond:
            connector_to_file_config.insert(super_job.config)
            connector_to_file.insert(super_job.vacancies)
        else:
            print("Нет данных по запросу.\n")

    # Работа с файлом
    elif user_answer == user_questions[0]["3.Работа с файлом\n"]:

        # Валидация файла
        if connector_to_file.validate() is True:

            while True:

                # Меню взаимодействия при работе с файлом
                print(*user_questions[1])
                user_answer = input()

                # Выйти в основное меню
                if user_answer == user_questions[1]["3.Выйти в команды верхнего меню\n"]:
                    break

                # Выбор данных их файла
                elif user_answer == user_questions[1][" 1.Выбор данных их файла\n"]:

                    while True:

                        # Меню для выборки ключа поиска
                        print("Выберите поле для поиска.\n")
                        print(*user_search)
                        user_answer_key = input()

                        if user_answer_key in str((1, 2, 3, 4, 5, 6, 7, 8)):
                            break
                        else:
                            print("! Некорректная команда ввода !\n")

                    # Ввод значение поля поиска
                    user_answer_value = input("Введите значение. Регистр важен.\n")
                    search_filter = {user_search_answers[user_answer_key]: user_answer_value}
                    print(connector_to_file.select(search_filter))
                    founded_vacancies = connector_to_file.select(search_filter)


                    input("Для продолжения нажмите Enter...")

                # Удаление данных их файла
                elif user_answer == user_questions[1]["2.Удаление данных их файла\n"]:

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
                    print(f"Было удалено:{connector_to_file.delete(search_filter)} вакансий.")
                    input("Удаление выполнено. Для продолжения нажмите Enter...")

                else:
                    print(*user_questions[3])

    # Работа с вакансиями
    elif user_answer == user_questions[0]["4.Работа с вакансиями\n"]:

        # Валидация файла
        if connector_to_file.validate() is True:
            get_last_status_request = (connector_to_file_config.select({"*": "*"}))[0]["last request"]
            print(get_last_status_request)
            while True:

                # Меню взаимодействия при работе с вакансиями
                print(*user_questions[2])
                user_answer = input()

                # Выйти в основное меню
                if user_answer == user_questions[2]["4.Выйти в команды верхнего меню\n"]:
                    break

                # Не сделано
                elif user_answer == user_questions[2][" 1.Вывести произвольное количество вакансий из файла\n"]:
                    print("Вывести произвольное количество вакансий из файла")

                # Вывести N самых высокооплачиваемые вакансии
                elif user_answer == user_questions[2]["2.Вывести N самых высокооплачиваемые вакансии\n"]:
                    count_of_vacancies = int(input("Ввести искомое количество вакансий.\n"
                                                   "Если число больше найденных вакансий, будут выведены все.\n"))

                    # Обработка для HEAD HUNTER
                    if get_last_status_request == "Последний запрос был к HEAD HUNTER":

                        all_vacancy = connector_to_file.select({"*": "*"})
                        sort_dict = []
                        for vacancy in all_vacancy:
                            vacancy_instance = HHVacancy(vacancy)
                            sort_dict.append(vacancy_instance)

                        # Сортировка списка с экземплярами вакансий
                        sort_dict.sort(reverse=True)
                        for vacancy in sort_dict[:count_of_vacancies]:
                            print(vacancy)

                    # Обработка для SUPER JOB
                    if get_last_status_request == "Последний запрос был к SUPER JOB":

                        all_vacancy = connector_to_file.select({"*": "*"})
                        sort_dict = []
                        for vacancy in all_vacancy:
                            vacancy_instance = SJVacancy(vacancy)
                            sort_dict.append(vacancy_instance)

                        # Сортировка списка с экземплярами вакансий
                        sort_dict.sort(reverse=True)
                        for vacancy in sort_dict[:count_of_vacancies]:
                            print(vacancy)

                # Гибкий поиск по вакансиям
                elif user_answer == user_questions[2]["3.Глубокий поиск по вакансиям\n"]:

                    while True:

                        # Запрос на критерии поиска и поиск по этим критериям
                        print("Выбрать поле для поиска.\n")
                        # Меню с вариантами ключей поиска
                        print(*user_search_vacancies)
                        user_answer_key = input("Введите значение для поиска.")

                        if user_answer_key in str((1, 2, 3, 4, 5)):
                            break
                        else:
                            print("! Некорректная команда ввода !\n")

                    user_answer_value = input("Введите значение для поиска. Ищет совпадения. Регистр важен.\n")
                    search_filter = {user_search_answers_vacancies[user_answer_key]: user_answer_value}

                    # Обработка для HEAD HUNTER
                    if type_of_request == 1:
                        all_vacancy = connector_to_file.select({"*": "*"})

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

















