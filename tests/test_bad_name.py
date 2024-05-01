import pytest
import time
from pages.registration_page import RegistrationPage
import allure

@pytest.mark.parametrize("name", [('a'),
                                  ('aaaaa'), ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
                                  ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaazzzzzzzzzzzzz'), ('1aaaaaa')])
def test_input_bad_name(name, web_browser):
    with allure.step('Открыть страницу регистрации'):
        app = RegistrationPage(web_browser)

    with allure.step('Ввести значение в поле Имя пользователя'):
        app.shadow_input_name(name)
        app.shadow_form().click()
        time.sleep(1)

    with allure.step('Проверить значение ошибки поля Имя пользователя'):
        assert app.shadow_span_name().text == 'Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы'
