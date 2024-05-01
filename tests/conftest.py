import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
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
    time.sleep(5)

    yield driver

    attach.add_screenshot(driver)
    attach.add_logs(driver)
    attach.add_html(driver)
    attach.add_video(driver)


    driver.quit()