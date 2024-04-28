import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.mark.parametrize("level, password", [(1, 'a'), (1, 'aaaaaaaa'), (2, 'aaaaaaaa1Z'),
                                             (3, 'aaaaaaaa12ZXC#')])
def test_password(level, password):
    driver = webdriver.Chrome()
    driver.get("https://koshelek.ru/authorization/signup")
    time.sleep(4)

    shadow_host = driver.find_element(By.CLASS_NAME, "remoteComponent")
    shadow_root = shadow_host.shadow_root
    shadow_content_form = shadow_root.find_element(By.CSS_SELECTOR, 'form')

    shadow_content_div_password = shadow_content_form.find_element(By.XPATH, ".//div[@data-wi='password']")

    shadow_content_input_password = shadow_content_div_password.find_element(By.CSS_SELECTOR, "input").send_keys(f'{password}')
    time.sleep(1)

    shadow_content_text = shadow_content_div_password.find_element(By.XPATH, ".//span[contains(text(), 'аро')]")
    print(f'\r\n\r\nTEXT = {shadow_content_text.text}')
    # assert shadow_content_text.text == 'Имя пользователя уже занято'

    driver.quit()
