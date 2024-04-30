import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.mark.parametrize("char",
                         [('ж'), ('Ж'), ('~'), ('@'), ('#'), ('$'), ('%'), ('^'), ('&'), ('*'), ('('), (')'), ('-'),
                          ('+'), ('\\'), ('|'), ('/'), ('?'), ('.'), (',')])
def test_bad_char_name(char):
    driver = webdriver.Chrome()
    driver.get("https://koshelek.ru/authorization/signup")
    time.sleep(7)

    shadow_host = driver.find_element(By.CLASS_NAME, "remoteComponent")
    shadow_root = shadow_host.shadow_root
    shadow_content_form = shadow_root.find_element(By.CSS_SELECTOR, 'form')

    shadow_content_div_name = shadow_content_form.find_element(By.XPATH, ".//div[@data-wi='user-name']")

    shadow_content_input_name = shadow_content_div_name.find_element(By.CSS_SELECTOR, "input").send_keys(f'Name{char}')
    time.sleep(1)

    shadow_content1 = shadow_content_div_name.find_element(By.XPATH, ".//span[@class='k-text']")

    assert shadow_content1.text == f'Введены недопустимые символы: {char}'

    time.sleep(1)
    driver.quit()
