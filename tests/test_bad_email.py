import pytest
from pages.registration_page import RegistrationPage
import allure


# @pytest.mark.parametrize("email", [('user')])
@pytest.mark.parametrize("email",
                         [('user'), ('user@'), ('user@mail'), ('user@mail.'), ('user@mail.1'), ('user@mail.a')])
def test_input_bad_email(email, web_browser):
    with allure.step('Открыть страницу регистрации'):
        app = RegistrationPage(web_browser)

    with allure.step('Ввести значение в поле Электронная почта'):
        app.shadow_input_email(email)
        app.shadow_form().click()

    with allure.step('Проверить значение ошибки поля Электронная почта'):
        assert app.shadow_span_email().text == 'Формат e-mail: username@test.ru'
