import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.mark.parametrize("name", [('a'),
                                  ('aaaaa'), ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
                                  ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaazzzzzzzzzzzzz'), ('1aaaaaa'),
                                  ('abcdef|'), ('abcdef.'), ('abcdef,'), ('abcdef?'), ('abcdef/'), ('abcdef>'),
                                  ('abcdef:'), ('abcdef;'), ('abcdef,'), ('abcdef~'), ('abcdef!'), ('abcdef@'),
                                  ('abcdef#'), ('abcdef$'), ('abcdef%'), ('abcdef^'), ('abcdef&'), ('abcdef%'),
                                  ('abcdef*'), ('abcdef('), ('abcdef)'), ('abcdef-'), ('abcdef+'), ('abcdef=')])
def test_bad_name(name):
    driver = webdriver.Chrome()
    driver.get("https://koshelek.ru/authorization/signup")
    time.sleep(7)

    shadow_host = driver.find_element(By.CLASS_NAME, "remoteComponent")
    shadow_root = shadow_host.shadow_root
    shadow_content = shadow_root.find_element(By.CSS_SELECTOR, 'form')
    shadow_content1 = shadow_content.find_element(By.XPATH, ".//*[text()='Имя пользователя']//..//input").send_keys(f'{name}')
    shadow_content1 = shadow_content.find_element(By.XPATH, ".//*[text()='Электронная почта']//..//input").click()

    shadow_host1 = driver.find_element(By.CLASS_NAME, "remoteComponent")
    shadow_root1 = shadow_host1.shadow_root
    shadow_content = shadow_root.find_element(By.CSS_SELECTOR, 'form')
    shadow_content1 = shadow_content.find_element(By.XPATH, ".//span[contains(text(), 'Допустимые символы')]")

    assert shadow_content1.text == 'Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы'

    time.sleep(1)
    driver.quit()



# @pytest.mark.parametrize("email", [('user')])
@pytest.mark.parametrize("email", [('user'), ('user@'), ('user@mail'), ('user@mail.'), ('user@mail.1'), ('user@mail.a')])
def test_name(email):
    driver = webdriver.Chrome()
    driver.get("https://koshelek.ru/authorization/signup")
    time.sleep(7)

    shadow_host = driver.find_element(By.CLASS_NAME, "remoteComponent")
    shadow_root = shadow_host.shadow_root
    shadow_content = shadow_root.find_element(By.CSS_SELECTOR, 'form')
    shadow_content1 = shadow_content.find_element(By.XPATH, ".//*[text()='Имя пользователя']//..//input").send_keys(f'aaaaaaaa')
    shadow_content1 = shadow_content.find_element(By.XPATH, ".//*[text()='Электронная почта']//..//input").send_keys(f'{email}')
    shadow_content1 = shadow_content.find_element(By.XPATH, ".//*[text()='Пароль']//..//input").click()

    shadow_host1 = driver.find_element(By.CLASS_NAME, "remoteComponent")
    shadow_root1 = shadow_host1.shadow_root
    shadow_content = shadow_root.find_element(By.CSS_SELECTOR, 'form')
    shadow_content1 = shadow_content.find_element(By.XPATH, ".//span[contains(text(), 'Формат e-mail')]")

    assert shadow_content1.text == 'Формат e-mail: username@test.ru'

    time.sleep(1)
    driver.quit()

