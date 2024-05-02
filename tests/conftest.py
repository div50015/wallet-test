import pytest
from selenium import webdriver
import time
from utils import attach

# @pytest.fixture( autouse=True)
# def driver_management():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(10)
#     driver.get("https://koshelek.ru/authorization/signup")
#     # time.sleep(5)
#
#     yield driver
#
#     driver.quit()

@pytest.fixture(scope='function', autouse=True)
def web_browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://koshelek.ru/authorization/signup")
    time.sleep(7)

    yield driver

    attach.add_screenshot(driver)
    attach.add_logs(driver)
    attach.add_html(driver)

    driver.quit()