from src.engine_classes import *
from src.utils import *
from src.connector import Connector
from src.jobs_classes import Vacancy
import json
import os
user_answer = ""
user_question = False

while not user_question:
    print("""Выберите действие:
    1.Запросить данные с сайта HEAD HUNTER
    2.Запросить данные с сайта SUPER JOB       
    """)
    user_answer = input()
    if user_answer in ('stop', 'стоп'):
        break
    if user_answer in ("1", "2"):
        user_question = True


# обработка запросов с сайтов
if user_answer == "1":
    print("Делаем запрос с HEAD HUNTER")
elif user_answer == "2":
    print("Делаем запрос с SUPER JOB")



















