import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope='function', autouse=True)
def driver_management():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://koshelek.ru/authorization/signup")
    # time.sleep(5)


    yield driver

    driver.quit()

# @pytest.fixture(scope='function', autouse=True)
# def driver_config(request):
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(10)
#     driver.get("https://koshelek.ru/authorization/signup")
#     # time.sleep(5)
#     request.cls.driver = driver
#
#     yield driver
#
#     driver.quit()