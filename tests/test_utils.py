from src.utils import *
import pytest


@pytest.fixture()
def all_vacancies():
    all_vacancies = [
        {
            "name": "fullstack разработчик",
            "url": "https://api.hh.ru/vacancies/78464455?host=hh.ru",
            "responsibility": "разработка нового функционала. поддержка легаси. реверс-инжиниринг. исправление багов. комментирование / составление документации. участвовать в принятии технических решений.",
            "town": "нижний новгород",
            "employer": "ptscrm",
            "requirement": "знание python 3+ (опыт работы с django 3 от 1 года , drf, fastapi) - mysql - умение писать сложные запросы, пользоваться...",
            "salary_from": "120000",
            "salary_to": "0"
        },
        {
            "name": "data scientist (middle/senior)",
            "url": "https://api.hh.ru/vacancies/70163749?host=hh.ru",
            "responsibility": "моделирование и обработка данных на python для извлечения бизнес-ценности из данных. построение воспроизводимых и переиспользуемых решений для работы с...",
            "town": "москва",
            "employer": "rubbles",
            "requirement": "опыт использования ml библиотек на python (бустинг, нейронные сети и др.) и понимание особенностей реализации различных аспектов алгоритмов в коде. ",
            "salary_from": "0",
            "salary_to": "400000"
        },
        {
            "name": "devops инженер",
            "url": "https://api.hh.ru/vacancies/78991603?host=hh.ru",
            "responsibility": "подготовка пакетов deb и rpm для системы автоматического развёртывания кластеров. доработка python скриптов для системы автоматического развёртывания кластеров. ",
            "town": "санкт-петербург",
            "employer": "балтинфоком",
            "requirement": "умение красиво решать нестандартные задачи. математический склад ума. умение работать в команде. внимательное отношение к своему и чужому коду. ",
            "salary_from": "100000",
            "salary_to": "0"
        },
    ]
    return all_vacancies


def test_format_text_1():
    """ Проверка обработки срочных в собранных данных """
    test_case_1 = "null"
    test_case_2 = "Данных нет"
    assert(format_text(test_case_1)) == test_case_2


def test_format_text_2():
    """ Проверка обработки срочных в собранных данных """
    test_case_1 = "Тестовые данные<highlighttext>."
    test_case_2 = "Тестовые данные."
    assert(format_text(test_case_1)) == test_case_2


def test_get_best_hh_vacancies(all_vacancies):
    """ Проверка на корректность поиска количества лучших вакансий"""
    founded = get_best_hh_vacancies(all_vacancies, 2)
    assert(len(founded)) == 2


def test_get_best_sj_vacancies(all_vacancies):
    """ Проверка на корректность поиска количества лучших вакансий"""
    founded = get_best_sj_vacancies(all_vacancies, 2)
    assert(len(founded)) == 2


def test_print_info(capsys):
    """ Проверка на корректность вывода информации (используем при работе с файлом)"""
    print_info("test")
    captured = capsys.readouterr()
    assert captured.out == "test\n" + "--------------------------------------\n"


def test_get_deep_query_hh_vacancies_1(capsys, all_vacancies):
    """ Проверка на действия пользователя при глубоком поиске"""
    get_deep_query_hh_vacancies(all_vacancies, "", "1")
    captured = capsys.readouterr()
    assert captured.out == 'Для поиска введено пустое поле.\n\n'
    get_deep_query_hh_vacancies(all_vacancies, "", "2")
    captured = capsys.readouterr()
    assert captured.out == 'Для поиска введено пустое поле.\n\n'
    get_deep_query_hh_vacancies(all_vacancies, "", "3")
    captured = capsys.readouterr()
    assert captured.out == 'Для поиска введено пустое поле.\n\n'
    get_deep_query_hh_vacancies(all_vacancies, "", "4")
    captured = capsys.readouterr()
    assert captured.out == 'Для поиска введено пустое поле.\n\n'
    get_deep_query_hh_vacancies(all_vacancies, "", "5")
    captured = capsys.readouterr()
    assert captured.out == 'Для поиска введено пустое поле.\n\n'


def test_get_deep_query_sj_vacancies_1(capsys, all_vacancies):
    """ Проверка на действия пользователя при глубоком поиске"""
    get_deep_query_hh_vacancies(all_vacancies, "", "1")
    captured = capsys.readouterr()
    assert captured.out == 'Для поиска введено пустое поле.\n\n'
    get_deep_query_hh_vacancies(all_vacancies, "", "2")
    captured = capsys.readouterr()
    assert captured.out == 'Для поиска введено пустое поле.\n\n'
    get_deep_query_hh_vacancies(all_vacancies, "", "3")
    captured = capsys.readouterr()
    assert captured.out == 'Для поиска введено пустое поле.\n\n'
    get_deep_query_hh_vacancies(all_vacancies, "", "4")
    captured = capsys.readouterr()
    assert captured.out == 'Для поиска введено пустое поле.\n\n'
    get_deep_query_hh_vacancies(all_vacancies, "", "5")
    captured = capsys.readouterr()
    assert captured.out == 'Для поиска введено пустое поле.\n\n'


def test_get_deep_query_hh_vacancies_2(capsys, all_vacancies):
    """ Проверка на действия пользователя при глубоком поиске"""

    get_deep_query_hh_vacancies(all_vacancies, "нижний новгород", "3")
    captured = capsys.readouterr()
    expected = ('Данные с HeadHunter\n'
     'Наименование: fullstack разработчик\n'
     'Ссылка: https://api.hh.ru/vacancies/78464455?host=hh.ru\n'
     'Описание: разработка нового функционала. поддержка легаси. '
     'реверс-инжиниринг. исправление багов. комментирование / составление '
     'документации. участвовать в принятии технических решений.\n'
     'Город: нижний новгород\n'
     'Компания: ptscrm\n'
     'Требования: знание python 3+ (опыт работы с django 3 от 1 года , drf, '
     'fastapi) - mysql - умение писать сложные запросы, пользоваться...\n'
     'ЗП от: 120000\n'
     'ЗП до: 0\n'
     '\n')
    assert captured.out == expected


def test_get_deep_query_sj_vacancies_2(capsys, all_vacancies):
    """ Проверка на действия пользователя при глубоком поиске"""

    get_deep_query_sj_vacancies(all_vacancies, "нижний новгород", "3")
    captured = capsys.readouterr()
    expected = ('Данные с SuperJob\n'
     'Наименование: fullstack разработчик\n'
     'Ссылка: https://api.hh.ru/vacancies/78464455?host=hh.ru\n'
     'Описание: разработка нового функционала. поддержка легаси. '
     'реверс-инжиниринг. исправление багов. комментирование / составление '
     'документации. участвовать в принятии технических решений.\n'
     'Город: нижний новгород\n'
     'Компания: ptscrm\n'
     'Требования: знание python 3+ (опыт работы с django 3 от 1 года , drf, '
     'fastapi) - mysql - умение писать сложные запросы, пользоваться...\n'
     'ЗП от: 120000\n'
     'ЗП до: 0\n'
     '\n')
    assert captured.out == expected


def test_get_deep_query_hh_vacancies_3(capsys, all_vacancies):
    """ Проверка на действия пользователя при глубоком поиске"""
    get_deep_query_hh_vacancies(all_vacancies, "devops инженер", "1")
    captured = capsys.readouterr()
    expected = ('Данные с HeadHunter\n'
 'Наименование: devops инженер\n'
 'Ссылка: https://api.hh.ru/vacancies/78991603?host=hh.ru\n'
 'Описание: подготовка пакетов deb и rpm для системы автоматического '
 'развёртывания кластеров. доработка python скриптов для системы '
 'автоматического развёртывания кластеров. \n'
 'Город: санкт-петербург\n'
 'Компания: балтинфоком\n'
 'Требования: умение красиво решать нестандартные задачи. математический склад '
 'ума. умение работать в команде. внимательное отношение к своему и чужому '
 'коду. \n'
 'ЗП от: 100000\n'
 'ЗП до: 0\n'
 '\n')
    assert captured.out == expected


def test_get_deep_query_sj_vacancies_3(capsys, all_vacancies):
    """ Проверка на действия пользователя при глубоком поиске"""
    get_deep_query_sj_vacancies(all_vacancies, "devops инженер", "1")
    captured = capsys.readouterr()
    expected = ('Данные с SuperJob\n'
                'Наименование: devops инженер\n'
                'Ссылка: https://api.hh.ru/vacancies/78991603?host=hh.ru\n'
                'Описание: подготовка пакетов deb и rpm для системы автоматического '
                'развёртывания кластеров. доработка python скриптов для системы '
                'автоматического развёртывания кластеров. \n'
                'Город: санкт-петербург\n'
                'Компания: балтинфоком\n'
                'Требования: умение красиво решать нестандартные задачи. математический склад '
                'ума. умение работать в команде. внимательное отношение к своему и чужому '
                'коду. \n'
                'ЗП от: 100000\n'
                'ЗП до: 0\n'
                '\n')
    assert captured.out == expected


def test_get_deep_query_hh_vacancies_4(capsys, all_vacancies):
    """ Проверка на действия пользователя при глубоком поиске"""

    get_deep_query_hh_vacancies(all_vacancies, "rubbles", "4")
    captured = capsys.readouterr()
    expected = ('Данные с HeadHunter\n'
 'Наименование: data scientist (middle/senior)\n'
 'Ссылка: https://api.hh.ru/vacancies/70163749?host=hh.ru\n'
 'Описание: моделирование и обработка данных на python для извлечения '
 'бизнес-ценности из данных. построение воспроизводимых и переиспользуемых '
 'решений для работы с...\n'
 'Город: москва\n'
 'Компания: rubbles\n'
 'Требования: опыт использования ml библиотек на python (бустинг, нейронные '
 'сети и др.) и понимание особенностей реализации различных аспектов '
 'алгоритмов в коде. \n'
 'ЗП от: 0\n'
 'ЗП до: 400000\n'
 '\n')
    assert captured.out == expected


def test_get_deep_query_sj_vacancies_4(capsys, all_vacancies):
    """ Проверка на действия пользователя при глубоком поиске"""
    get_deep_query_sj_vacancies(all_vacancies, "rubbles", "4")
    captured = capsys.readouterr()
    expected = ('Данные с SuperJob\n'
 'Наименование: data scientist (middle/senior)\n'
 'Ссылка: https://api.hh.ru/vacancies/70163749?host=hh.ru\n'
 'Описание: моделирование и обработка данных на python для извлечения '
 'бизнес-ценности из данных. построение воспроизводимых и переиспользуемых '
 'решений для работы с...\n'
 'Город: москва\n'
 'Компания: rubbles\n'
 'Требования: опыт использования ml библиотек на python (бустинг, нейронные '
 'сети и др.) и понимание особенностей реализации различных аспектов '
 'алгоритмов в коде. \n'
 'ЗП от: 0\n'
 'ЗП до: 400000\n'
 '\n')
    assert captured.out == expected


def test_get_deep_query_hh_vacancies_5(capsys, all_vacancies):
    """ Проверка на действия пользователя при глубоком поиске"""
    get_deep_query_hh_vacancies(all_vacancies, "опыт использования ml библиотек на python", "5")
    captured = capsys.readouterr()
    expected = ('Данные с HeadHunter\n'
 'Наименование: data scientist (middle/senior)\n'
 'Ссылка: https://api.hh.ru/vacancies/70163749?host=hh.ru\n'
 'Описание: моделирование и обработка данных на python для извлечения '
 'бизнес-ценности из данных. построение воспроизводимых и переиспользуемых '
 'решений для работы с...\n'
 'Город: москва\n'
 'Компания: rubbles\n'
 'Требования: опыт использования ml библиотек на python (бустинг, нейронные '
 'сети и др.) и понимание особенностей реализации различных аспектов '
 'алгоритмов в коде. \n'
 'ЗП от: 0\n'
 'ЗП до: 400000\n'
 '\n')
    assert captured.out == expected


def test_get_deep_query_sj_vacancies_5(capsys, all_vacancies):
    """ Проверка на действия пользователя при глубоком поиске"""
    get_deep_query_sj_vacancies(all_vacancies, "опыт использования ml библиотек на python", "5")
    captured = capsys.readouterr()
    expected = ('Данные с SuperJob\n'
 'Наименование: data scientist (middle/senior)\n'
 'Ссылка: https://api.hh.ru/vacancies/70163749?host=hh.ru\n'
 'Описание: моделирование и обработка данных на python для извлечения '
 'бизнес-ценности из данных. построение воспроизводимых и переиспользуемых '
 'решений для работы с...\n'
 'Город: москва\n'
 'Компания: rubbles\n'
 'Требования: опыт использования ml библиотек на python (бустинг, нейронные '
 'сети и др.) и понимание особенностей реализации различных аспектов '
 'алгоритмов в коде. \n'
 'ЗП от: 0\n'
 'ЗП до: 400000\n'
 '\n')
    assert captured.out == expected
