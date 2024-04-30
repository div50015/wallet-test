import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# @pytest.mark.parametrize("level, password", [(1, 'a')])
@pytest.mark.parametrize("level, password",
                         [(1, 'a'), (2, 'aaaaaaaa'), (2, 'aaaaaaaA'), (2, 'aaaaaaa1'), (2, 'aaaaaaa#'), (2, 'aaaaaaA1'),
                          (2, 'aaaaaaA#'), (2, 'aaaaaa1#')])
def test_bad_password(level, password):
    driver = webdriver.Chrome()
    driver.get("https://koshelek.ru/authorization/signup")
    time.sleep(7)

    shadow_host = driver.find_element(By.CLASS_NAME, "remoteComponent")
    shadow_root = shadow_host.shadow_root
    shadow_content_form = shadow_root.find_element(By.CSS_SELECTOR, 'form')

    shadow_content_div_password = shadow_content_form.find_element(By.XPATH, ".//div[@data-wi='password']")

    shadow_content_input_password = shadow_content_div_password.find_element(By.CSS_SELECTOR, "input").send_keys(f'{password}')
    shadow_content = shadow_content_form.click()
    time.sleep(1)


    shadow_content_text = shadow_content_div_password.find_element(By.XPATH, ".//span[@class='k-text']")
    # vv = shadow_content_form.find_elements(By.CSS_SELECTOR, "span")
    #   # print(f'\r\n\r\nTEXT = {shadow_content_text}')
    # for v in vv:
    #     print(f'v = {v.text}')
    if level == 1:
        assert shadow_content_text.text == 'Пароль должен содержать минимум 8 символов'
    if level == 2:
        assert shadow_content_text.text == 'Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры'

    driver.quit()
