import pytest
from pages.registration_page import RegistrationPage
import allure


@pytest.mark.parametrize("char",
                         [('ж'), ('Ж'), ('~'), ('@'), ('#'), ('$'), ('%'), ('^'), ('*'), ('('), (')'), ('-'),
                          ('+'), ('\\'), ('|'), ('?'), ('.'), (',')])
def test_input_bad_char_name(char, web_browser):
    with allure.step('Открыть страницу регистрации'):
        app = RegistrationPage(web_browser)

    with allure.step('Ввести значение в поле Имя пользователя'):
        app.shadow_input_char_name(char)

    with allure.step('Проверить значение ошибки поля Имя пользователя'):
        assert app.shadow_span_name().text == f'Введены недопустимые символы: {char}'
