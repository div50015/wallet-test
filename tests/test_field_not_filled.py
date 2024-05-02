import time
from pages.registration_page import RegistrationPage
import allure


def test_input_null_name(web_browser):
    with allure.step('Открыть страницу регистрации'):
        app = RegistrationPage(web_browser)

    with allure.step('Ввести значение в поле Имя пользователя'):
        app.shadow_input_name('\n')
        time.sleep(1)

    with allure.step('Проверить значение ошибки полей Имя пользователя Электронная почта Пароль и Я согласен'):
        assert app.shadow_span_name().text == 'Поле не заполнено'
        assert app.shadow_span_email().text == 'Поле не заполнено'
        assert app.shadow_span_password().text == 'Поле не заполнено'
        assert app.shadow_span_password().text == 'Поле не заполнено'
        assert app.shadow_span_checkbox().get_attribute('class') == 'v-input v-input--has-state v-input--hide-details v-input--dense theme--light v-input--selection-controls v-input--checkbox error--text'

