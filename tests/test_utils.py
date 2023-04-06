from src.utils import *
import mock
import builtins


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
