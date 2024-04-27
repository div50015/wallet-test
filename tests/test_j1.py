import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.mark.parametrize("name", [('username')])
def test_bad_name(name):
    driver = webdriver.Chrome()
    driver.get("https://koshelek.ru/authorization/signup")
    time.sleep(7)

    shadow_host = driver.find_element(By.CLASS_NAME, "remoteComponent")
    shadow_root = shadow_host.shadow_root
    shadow_content = shadow_root.find_element(By.CSS_SELECTOR, 'form')
    shadow_content1 = shadow_content.find_element(By.XPATH, ".//*[text()='Имя пользователя']//..//input").send_keys(f'{name}')
    shadow_content2 = shadow_content.find_element(By.XPATH, ".//*[text()='Электронная почта']//..//input").click()

    shadow_host1 = driver.find_element(By.CLASS_NAME, "remoteComponent")
    shadow_root1 = shadow_host1.shadow_root
    shadow_content3 = shadow_root.find_element(By.CSS_SELECTOR, 'form')
    shadow_content4 = shadow_content3.find_elements(By.XPATH, ".//span[contains(text(), ' ')]")
    print(f'cont = {shadow_content4}')
    i = 0
    for v in shadow_content4:
        i = i + 1
        print(f'cont{i} = {v.text}')

    assert shadow_content4[0].text == 'Имя пользователя уже занято'

    time.sleep(1)
    driver.quit()
