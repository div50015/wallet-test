import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# @pytest.mark.parametrize("level, password", [(1, 'a')])
@pytest.mark.parametrize("code", [('1'), ('123'), ('123456789'), ('123456789123456789')])
def test_bad_ref_code(code):
    driver = webdriver.Chrome()
    driver.get("https://koshelek.ru/authorization/signup")
    time.sleep(7)

    shadow_host = driver.find_element(By.CLASS_NAME, "remoteComponent")
    shadow_root = shadow_host.shadow_root
    shadow_content_form = shadow_root.find_element(By.CSS_SELECTOR, 'form')

    shadow_content_div_password = shadow_content_form.find_element(By.XPATH, ".//div[@data-wi='password']")
    shadow_content_div_ref_code = shadow_content_form.find_element(By.XPATH, ".//div[@data-wi='referral']")
    # time.sleep(1)
    shadow_content_input_ref_kod = shadow_content_div_ref_code.find_element(By.CSS_SELECTOR, "input").send_keys(f'{code}')
    time.sleep(1)

    # shadow_content_input_password = shadow_content_div_password.find_element(By.CSS_SELECTOR, "input").click()
    shadow_content_text = shadow_content_div_ref_code.find_element(By.XPATH, ".//span[@class='k-text']")
    # vv = shadow_content_form.find_elements(By.CSS_SELECTOR, "span")
    #   # print(f'\r\n\r\nTEXT = {shadow_content_text}')
    # for v in vv:
    #     print(f'v = {v.text}')
    assert shadow_content_text.text == 'Неверный формат ссылки'

    driver.quit()
