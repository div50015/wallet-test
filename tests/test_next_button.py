import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_fieled_not_filled():
    driver = webdriver.Chrome()
    driver.set_window_size(1080,1080)
    driver.get("https://koshelek.ru/authorization/signup")
    time.sleep(5)

    shadow_host = driver.find_element(By.CLASS_NAME, "remoteComponent")
    shadow_root = shadow_host.shadow_root
    shadow_content_form = shadow_root.find_element(By.CSS_SELECTOR, 'form')

    shadow_content_div_name = shadow_content_form.find_element(By.XPATH, ".//div[@data-wi='user-name']")
    shadow_content_div_email = shadow_content_form.find_element(By.XPATH, ".//div[@data-wi='identificator']")
    shadow_content_div_password = shadow_content_form.find_element(By.XPATH, ".//div[@data-wi='password']")
    shadow_content_div_chekbox = shadow_content_form.find_element(By.XPATH, ".//div[@data-wi='user-agreement']")
    shadow_content_div_buton = shadow_content_form.find_element(By.XPATH, ".//div[@data-wi='submit-button']")

    shadow_content_button = shadow_content_div_buton.find_element(By.CSS_SELECTOR, "button").click()
    time.sleep(2)

    shadow_content_text1 = shadow_content_div_name.find_element(By.XPATH, ".//span[@class='k-text']")
    shadow_content_text2 = shadow_content_div_email.find_element(By.XPATH, ".//span[@class='k-text']")
    shadow_content_text3 = shadow_content_div_password.find_element(By.XPATH, ".//span[@class='k-text']")
    shadow_content_text4 = shadow_content_div_chekbox.find_element(By.XPATH, ".//div").get_attribute('class')
    # shadow_content_text4 = shadow_content_div_chekbox.find_element(By.XPATH, ".//div[@class='v-input']").get_attribute('class')
    # vv = shadow_content_form.find_elements(By.CSS_SELECTOR, "span")
    #   # print(f'\r\n\r\nTEXT = {shadow_content_text}')
    # for v in vv:
    #     print(f'v = {v.text}')
    assert shadow_content_text1.text == 'Поле не заполнено'
    assert shadow_content_text2.text == 'Поле не заполнено'
    assert shadow_content_text3.text == 'Поле не заполнено'
    assert shadow_content_text4 == 'v-input v-input--has-state v-input--hide-details v-input--dense theme--light v-input--selection-controls v-input--checkbox error--text'
    # print(shadow_content_text4)
    driver.quit()
