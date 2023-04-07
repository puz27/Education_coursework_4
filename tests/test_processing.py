import pytest
from src.jobs_classes import HHVacancy, SJVacancy
from src.connector import Connector


@pytest.fixture()
def vacancy():
    vacancy = {
        "name": "fullstack разработчик",
        "url": "https://api.hh.ru/vacancies/78464455?host=hh.ru",
        "responsibility": "разработка нового функционала",
        "town": "нижний новгород",
        "employer": "yandex",
        "requirement": "знание python",
        "salary_from": "120000",
        "salary_to": "0"
    }

    return vacancy


@pytest.fixture()
def vacancies():
    vacancies = [
            {
                "name": "Python",
                "town": "москва"
            },
            {
                "name": "fullstack разработчик",
                "town": "нижний новгород"
                }
        ]
    return vacancies


def test_vacancy_hh(vacancy):
    """ Проверка геттеров для экземпляра класса """
    vacancy_instance = HHVacancy(vacancy)
    assert vacancy_instance.name == "fullstack разработчик"
    assert vacancy_instance.url == "https://api.hh.ru/vacancies/78464455?host=hh.ru"
    assert vacancy_instance.responsibility == "разработка нового функционала"
    assert vacancy_instance.town == "нижний новгород"
    assert vacancy_instance.employer == "yandex"
    assert vacancy_instance.requirement == "знание python"
    assert vacancy_instance.salary_from == "120000"
    assert vacancy_instance.salary_to == "0"


def test_vacancy_sj(vacancy):
    """ Проверка геттеров для экземпляра класса """
    vacancy_instance = SJVacancy(vacancy)
    assert vacancy_instance.name == "fullstack разработчик"
    assert vacancy_instance.url == "https://api.hh.ru/vacancies/78464455?host=hh.ru"
    assert vacancy_instance.responsibility == "разработка нового функционала"
    assert vacancy_instance.town == "нижний новгород"
    assert vacancy_instance.employer == "yandex"
    assert vacancy_instance.requirement == "знание python"
    assert vacancy_instance.salary_from == "120000"
    assert vacancy_instance.salary_to == "0"


def test_connector_to_file(capsys):
    """ Проверка коннектора к файлу """
    connector_to_file = Connector("information.json")
    print(connector_to_file.data_file)
    captured = capsys.readouterr()
    assert captured.out == "information.json\n"


def test_connector_insert_select(vacancies):
    """ Проверка коннектора запись / выборка """
    connector_to_file = Connector("information.json")
    connector_to_file.insert(vacancies)
    datas = connector_to_file.select({"*": "*"})
    assert datas == vacancies


def test_connector_insert_delete(vacancies):
    """ Проверка коннектора запись / удаление """
    connector_to_file = Connector("information.json")
    connector_to_file.insert(vacancies)
    connector_to_file.delete({"*": "*"})
    datas = connector_to_file.select({"*": "*"})
    assert datas == []


def test_connector_validate_1(vacancies):
    """ Проверка коннектора / валидация файла """
    connector_to_file = Connector("information.json")
    connector_to_file.insert(vacancies)
    datas = connector_to_file.validate()
    assert datas is True


def test_connector_validate_2(capsys):
    """ Проверка коннектора / валидация файла """
    connector_to_file = Connector("broken_information.json")
    connector_to_file.validate()
    captured = capsys.readouterr()
    assert captured.out == "! Файл для обработки неверного формата, либо пустой !\n\n"


def test_hh_vacancy_name(capsys, vacancy):
    """ Проверка геттеров для экземпляра класса при запросе пользователя """
    user_answer_value, expected = "разработчик", "fullstack разработчик\n"
    vacancy_instance = HHVacancy(vacancy)
    if user_answer_value in vacancy_instance.name:
        print(vacancy_instance.name)
    captured = capsys.readouterr()
    assert captured.out == expected


def test_sj_vacancy_name(capsys, vacancy):
    """ Проверка геттеров для экземпляра класса при запросе пользователя """
    user_answer_value, expected = "разработчик", "fullstack разработчик\n"
    vacancy_instance = SJVacancy(vacancy)
    if user_answer_value in vacancy_instance.name:
        print(vacancy_instance.name)
    captured = capsys.readouterr()
    assert captured.out == expected


def test_hh_vacancy_responsibility(capsys, vacancy):
    """ Проверка геттеров для экземпляра класса при запросе пользователя """
    user_answer_value, expected = "разработка", "разработка нового функционала\n"
    vacancy_instance = HHVacancy(vacancy)
    if user_answer_value in vacancy_instance.responsibility:
        print(vacancy_instance.responsibility)
    captured = capsys.readouterr()
    assert captured.out == expected


def test_sj_vacancy_responsibility(capsys, vacancy):
    """ Проверка геттеров для экземпляра класса при запросе пользователя """
    user_answer_value, expected = "разработка", "разработка нового функционала\n"
    vacancy_instance = SJVacancy(vacancy)
    if user_answer_value in vacancy_instance.responsibility:
        print(vacancy_instance.responsibility)
    captured = capsys.readouterr()
    assert captured.out == expected


def test_hh_vacancy_town(capsys, vacancy):
    """ Проверка геттеров для экземпляра класса при запросе пользователя """
    user_answer_value, expected = "нижний новгород", "нижний новгород\n"
    vacancy_instance = HHVacancy(vacancy)
    if user_answer_value in vacancy_instance.town:
        print(vacancy_instance.town)
    captured = capsys.readouterr()
    assert captured.out == expected


def test_sj_vacancy_town(capsys, vacancy):
    """ Проверка геттеров для экземпляра класса при запросе пользователя """
    user_answer_value, expected = "нижний новгород", "нижний новгород\n"
    vacancy_instance = SJVacancy(vacancy)
    if user_answer_value in vacancy_instance.town:
        print(vacancy_instance.town)
    captured = capsys.readouterr()
    assert captured.out == expected


def test_hh_vacancy_employer(capsys, vacancy):
    """ Проверка геттеров для экземпляра класса при запросе пользователя """
    user_answer_value, expected = "yandex", "yandex\n"
    vacancy_instance = HHVacancy(vacancy)
    if user_answer_value in vacancy_instance.employer:
        print(vacancy_instance.employer)
    captured = capsys.readouterr()
    assert captured.out == expected


def test_sj_vacancy_employer(capsys, vacancy):
    """ Проверка геттеров для экземпляра класса при запросе пользователя """
    user_answer_value, expected = "yandex", "yandex\n"
    vacancy_instance = SJVacancy(vacancy)
    if user_answer_value in vacancy_instance.employer:
        print(vacancy_instance.employer)
    captured = capsys.readouterr()
    assert captured.out == expected


def test_hh_vacancy_requirement(capsys, vacancy):
    """ Проверка геттеров для экземпляра класса при запросе пользователя """
    user_answer_value, expected = "python", "знание python\n"
    vacancy_instance = HHVacancy(vacancy)
    if user_answer_value in vacancy_instance.requirement:
        print(vacancy_instance.requirement)
    captured = capsys.readouterr()
    assert captured.out == expected


def test_sj_vacancy_requirement(capsys, vacancy):
    """ Проверка геттеров для экземпляра класса при запросе пользователя """
    user_answer_value, expected = "python", "знание python\n"
    vacancy_instance = SJVacancy(vacancy)
    if user_answer_value in vacancy_instance.requirement:
        print(vacancy_instance.requirement)
    captured = capsys.readouterr()
    assert captured.out == expected
