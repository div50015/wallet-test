import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://koshelek.ru/authorization/signup'
    browser.config.timeout = 10.0
    browser.config.window_width = 1800
    browser.config.window_height = 1080

#    browser.config.type_by_js = True
    # закрытие сообщения о том что браузер запущен в отладочном режиме
    driver_options = webdriver.ChromeOptions()
    driver_options.add_experimental_option("excludeSwitches", ['enable-automation'])
#    driver_options.add_argument('--headless=new')
    browser.config.driver_options = driver_options

    yield

    browser.quit()