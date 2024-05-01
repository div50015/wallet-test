import pytest
from pages.registration_page import RegistrationPage
import allure
import time


@pytest.mark.parametrize("code", [('1'), ('123'), ('123456789'), ('123456789123456789')])
def test_input_bad_ref_code(code, web_browser):
    with allure.step('Открыть страницу регистрации'):
        app = RegistrationPage(web_browser)

    with allure.step('Ввести значение в поле Реферальный код'):
        app.shadow_input_ref_code(code)
        time.sleep(1)

    with allure.step('Проверить значение ошибки поля Реферальный код'):
        assert app.shadow_span_ref_code().text == 'Неверный формат ссылки'

