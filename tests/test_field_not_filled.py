import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_fieled_not_filled():
    driver = webdriver.Chrome()
    driver.set_window_size(1000,1080)
    driver.get("https://koshelek.ru/authorization/signup")
    time.sleep(7)

    shadow_host = driver.find_element(By.CLASS_NAME, "remoteComponent")
    shadow_root = shadow_host.shadow_root
    shadow_content_form = shadow_root.find_element(By.CSS_SELECTOR, 'form')

    shadow_content_div_name = shadow_content_form.find_element(By.XPATH, ".//div[@data-wi='user-name']")
    shadow_content_div_email = shadow_content_form.find_element(By.XPATH, ".//div[@data-wi='identificator']")
    shadow_content_div_password = shadow_content_form.find_element(By.XPATH, ".//div[@data-wi='password']")

    shadow_content = shadow_content_div_name.find_element(By.CSS_SELECTOR, "input").send_keys("\n")
    time.sleep(1)

    shadow_content_text1 = shadow_content_div_name.find_element(By.XPATH, ".//span[@class='k-text']")
    shadow_content_text2 = shadow_content_div_email.find_element(By.XPATH, ".//span[@class='k-text']")
    shadow_content_text3 = shadow_content_div_password.find_element(By.XPATH, ".//span[@class='k-text']")
    # vv = shadow_content_form.find_elements(By.CSS_SELECTOR, "span")
    #   # print(f'\r\n\r\nTEXT = {shadow_content_text}')
    # for v in vv:
    #     print(f'v = {v.text}')
    assert shadow_content_text1.text == 'Поле не заполнено'
    assert shadow_content_text2.text == 'Поле не заполнено'
    assert shadow_content_text3.text == 'Поле не заполнено'

    driver.quit()
