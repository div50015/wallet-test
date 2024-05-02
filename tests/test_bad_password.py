import pytest
from pages.registration_page import RegistrationPage
import allure


# @pytest.mark.parametrize("level, password", [(1, 'a')])
@pytest.mark.parametrize("level, password",
                         [(1, 'a'), (2, 'aaaaaaaa'), (2, 'aaaaaaaA'), (2, 'aaaaaaa1'), (2, 'aaaaaaa#'), (2, 'aaaaaaA#'),
                          (2, 'aaaaaa1#')])
def test_input_bad_password(level, password, web_browser):
    with allure.step('Открыть страницу регистрации'):
        app = RegistrationPage(web_browser)

    with allure.step('Ввести значение в поле Пароль'):
        app.shadow_input_password(password)
        app.shadow_form().click()

    with allure.step('Проверить значение ошибки поля Пароль'):
        if level == 1:
            assert app.shadow_span_password().text == 'Пароль должен содержать минимум 8 символов'
        if level == 2:
            assert app.shadow_span_password().text == 'Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры'
