import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# @pytest.mark.parametrize("email", [('user')])
@pytest.mark.parametrize("email", [('user'), ('user@'), ('user@mail'), ('user@mail.'), ('user@mail.1'), ('user@mail.a')])
def test_bad_email(email):
    driver = webdriver.Chrome()
    driver.get("https://koshelek.ru/authorization/signup")
    time.sleep(5)

    shadow_host = driver.find_element(By.CLASS_NAME, "remoteComponent")
    shadow_root = shadow_host.shadow_root
    shadow_content_form = shadow_root.find_element(By.CSS_SELECTOR, 'form')

    shadow_content_div_email = shadow_content_form.find_element(By.XPATH, ".//div[@data-wi='identificator']")

    shadow_content_input_email = shadow_content_div_email.find_element(By.CSS_SELECTOR, "input").send_keys(f'{email}')
    shadow_content = shadow_content_form.click()
    time.sleep(1)


    shadow_content1 = shadow_content_div_email.find_element(By.XPATH, ".//span[@class='k-text']")

    assert shadow_content1.text == 'Формат e-mail: username@test.ru'

    driver.quit()
