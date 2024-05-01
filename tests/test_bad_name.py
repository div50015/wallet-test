import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.registration_page import RegistrationPage
import allure

# @pytest.mark.parametrize("name", [('a')])
# @pytest.mark.parametrize("name", [('a'),
#                                   ('aaaaa'), ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
#                                   ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaazzzzzzzzzzzzz'), ('1aaaaaa')])
# def test_bad_name(name, driver_management):
#     # driver = webdriver.Chrome()
#     # driver.get("https://koshelek.ru/authorization/signup")
#     # time.sleep(5)
#     driver = driver_management
#     shadow_host = driver.find_element(By.CLASS_NAME, "remoteComponent")
#     shadow_root = shadow_host.shadow_root
#     shadow_content_form = shadow_root.find_element(By.CSS_SELECTOR, 'form')
#
#     shadow_content_div_name = shadow_content_form.find_element(By.XPATH, ".//div[@data-wi='user-name']")
#
#     shadow_content_input_name = shadow_content_div_name.find_element(By.CSS_SELECTOR, "input").send_keys(f'{name}')
#     shadow_content_input_email = shadow_content_form.click()
#     time.sleep(1)
#
#     shadow_content1 = shadow_content_div_name.find_element(By.XPATH, ".//span[@class='k-text']")
#
#     assert shadow_content1.text == 'Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы'
#
#     # driver.quit()

@pytest.mark.parametrize("name", [('a')])
def test_test(name, web_browser):
    with allure.step('Открыть страницу регистрации'):
        app = RegistrationPage(web_browser)

    with allure.step('Ввести значение в поле Имя пользователя'):
        app.shadow_input_name(name)
        app.shadow_form().click()
        time.sleep(1)

    with allure.step('Проверить значение ошибки поля Имя пользователя'):
        assert app.shadow_span_name().text == 'Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы'
