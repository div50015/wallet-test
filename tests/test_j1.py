import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.mark.parametrize("name", [('username')])
def test_bad_name(name):
    driver = webdriver.Chrome()
    driver.get("https://koshelek.ru/authorization/signup")
    time.sleep(4)

    shadow_host = driver.find_element(By.CLASS_NAME, "remoteComponent")
    shadow_root = shadow_host.shadow_root
    shadow_content_form = shadow_root.find_element(By.CSS_SELECTOR, 'form')

    shadow_content_div_name = shadow_content_form.find_element(By.XPATH, ".//div[@data-wi='user-name']")
    shadow_content_div_email = shadow_content_form.find_element(By.XPATH, ".//div[@data-wi='identificator']")

    shadow_content_input_name = shadow_content_div_name.find_element(By.CSS_SELECTOR, "input").send_keys(f'{name}')
    shadow_content_input_email = shadow_content_div_email.find_element(By.CSS_SELECTOR, "input").click()

    shadow_content_div_name = shadow_content_form.find_element(By.XPATH, ".//div[@data-wi='user-name']")
    shadow_content_text = shadow_content_div_name.find_elements(By.CSS_SELECTOR, "span")
    print(shadow_content_text[0].text)
    print(shadow_content_text[1].text)
    print(shadow_content_text[2].text)
    print(shadow_content_text[3].text)
    # shadow_host1 = driver.find_element(By.CLASS_NAME, "remoteComponent")
    # shadow_root1 = shadow_host1.shadow_root
    # shadow_content3 = shadow_root.find_element(By.CSS_SELECTOR, 'form')
    # shadow_content3 = shadow_content.find_elements(By.CSS_SELECTOR, ".//div[data-wi='message']").find_elements(By.CSS_SELECTOR, "span")
    # print(f'cont = {shadow_content3.text}')
    # i = 0
    # for v in shadow_content4:
    #     i = i + 1
    #     print(f'cont{i} = {v.text}')

    # assert shadow_content4[0].text == 'Имя пользователя уже занято'

    time.sleep(5)
    driver.quit()
