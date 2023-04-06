from src.utils import *
import mock
import builtins
import pytest


@pytest.fixture()
def all_vacancies():
    all_vacancies = [
        {
            "name": "Разработчик Python",
            "url": "https://api.hh.ru/vacancies/78473911?host=hh.ru",
            "responsibility": "Тест",
            "town": "Москва",
            "employer": "Нетопия",
            "requirement": "Тест",
            "salary_from": "200000",
            "salary_to": "250000"
        },
        {
            "name": "Разработчик Python",
            "url": "https://api.hh.ru/vacancies/77871173?host=hh.ru",
            "responsibility": "Тест",
            "town": "Санкт-Петербург",
            "employer": "Единая Информационная Система ЖКХ",
            "requirement": "Тест",
            "salary_from": "90000",
            "salary_to": "150000"
        },
        {
            "name": "Python-разработчик (Junior)",
            "url": "https://api.hh.ru/vacancies/78779580?host=hh.ru",
            "responsibility": "Участвовать в разработке алгоритмов торговых ботов и анализировать их эффективность. Продумывать архитектуры нейросетей и обучать их, применительно к трейдингу. ",
            "town": "Москва",
            "employer": "Щербин Алексей Сергеевич",
            "requirement": "Знание языка Python. Опыт работы с PostgreSQL. Знание основ работы с Git. Хорошее представление об асинхронном программировании. Желание расти и...",
            "salary_from": "40000",
            "salary_to": "60000"
        },
        {
            "name": "Junior Python Developer (удаленно)",
            "url": "https://api.hh.ru/vacancies/78896943?host=hh.ru",
            "responsibility": "Данных нет",
            "town": "Екатеринбург",
            "employer": "RLT (ООО Надежные Лояльные Технологии)",
            "requirement": "Будет плюсом: Опыт работы с библиотеками для работы с ботами (ТГ, ВК). Опыт использования docker/docker-compose.  3. ",
            "salary_from": "20000",
            "salary_to": "40000"
        }
    ]
    return all_vacancies


@pytest.fixture()
def best_vacancies():
    best_vacancies = [
        {
            "name": "Разработчик Python",
            "url": "https://api.hh.ru/vacancies/78473911?host=hh.ru",
            "responsibility": "Тест",
            "town": "Москва",
            "employer": "Нетопия",
            "requirement": "Тест",
            "salary_from": "200000",
            "salary_to": "250000"
        },
        {
            "name": "Разработчик Python",
            "url": "https://api.hh.ru/vacancies/77871173?host=hh.ru",
            "responsibility": "Тест",
            "town": "Санкт-Петербург",
            "employer": "Единая Информационная Система ЖКХ",
            "requirement": "Тест",
            "salary_from": "90000",
            "salary_to": "150000"
        }
    ]
    return best_vacancies


def test_format_text_1():
    test_case_1 = "null"
    test_case_2 = "Данных нет"
    assert(format_text(test_case_1)) == test_case_2


def test_format_text_2():
    test_case_1 = "Тестовые данные<highlighttext>."
    test_case_2 = "Тестовые данные."
    assert(format_text(test_case_1)) == test_case_2


# def test_check_user_answer_1():
#     with mock.patch.object(builtins, 'input', lambda _: '1'):
#         assert check_user_answer("Привет", "", 5) == "! Данные не переданы !\n"
#

def test_get_best_hh_vacancies_1(all_vacancies, best_vacancies):
    founded = get_best_hh_vacancies(all_vacancies, 2)
    assert(len(founded)) == 2


def test_get_best_sj_vacancies_1(all_vacancies, best_vacancies):
    founded = get_best_hh_vacancies(all_vacancies, 3)
    assert(len(founded)) == 3

# def test_get_deep_query_hh_vacancies(capsys):
#     test_all_vacancy = [
#         {
#         "name": "Разработчик Python",
#         "url": "https://api.hh.ru/vacancies/78473911?host=hh.ru",
#         "responsibility": "Работка backend части программного обеспечения. Разработка внутренних библиотек. Оптимизация узких мест в основной архитектуре продукта.",
#         "town": "Москва",
#         "employer": "Нетопия",
#         "requirement": "Владение Python (asyncio, aiohttp, pydantic, FastAPI). Опыт работы с рекурсиям, алгоритмами на деревьях (важно!). Понимание зачем нужен ООП. ",
#         "salary_from": "200000",
#         "salary_to": "250000"
#     },
#     {
#         "name": "Backend программист Python / Python Backend Developer",
#         "url": "https://api.hh.ru/vacancies/78542200?host=hh.ru",
#         "responsibility": "Typescript, Javascript в браузерных приложениях, React и Svelte для реактивности. Python + Starlette в серверных приложениях. GraphQL для обмена данными...",
#         "town": "Москва",
#         "employer": "Радиум",
#         "requirement": "Хорошее знание языка программирования Python. Знание SQL (PostgreSQL) на среднем уровне. Навык самостоятельного поиска информации и готовых решений. ",
#         "salary_from": "50000",
#         "salary_to": "0"
#     }
#     ]
#     user_answer_value = "Нетопия"
#     user_choice = "4"
#     expected = ' \n    "name": "Разработчик Python",\n        "url": "https://api.hh.ru/vacancies/78473911?host=hh.ru",\n        "responsibility": "Работа",\n        "town": "Москва",\n        "employer": "Нетопия",\n        "requirement": "Работа",\n        "salary_from": "200000",\n        "salary_to": "250000"\n        '
#     get_deep_query_hh_vacancies(test_all_vacancy, user_answer_value, user_choice)
#     captured = capsys.readouterr()
#     assert () == expected
#     assert captured.out == expected
