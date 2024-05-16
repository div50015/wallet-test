import pytest
import time
from pages.registration_page import RegistrationPage
import allure


@pytest.mark.parametrize("name", [('username')])
def test_input_busy_name(name, web_browser):
    with allure.step('Открыть страницу регистрации'):
        app = RegistrationPage(web_browser)

    with allure.step('Ввести значение в поле Имя пользователя'):
        app.shadow_input_name(name)
        app.shadow_form().click()
        # time.sleep(1)

    with allure.step('Проверить значение ошибки поля Имя пользователя'):
        assert app.shadow_span_busy_name().text == 'Имя пользователя уже занято'
