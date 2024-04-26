import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.mark.parametrize("name", [('a'), ('aaaaa'), ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
                                  ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'), '1aaaaaa',
                                  ('abcdef~'), ('abcdef!'), ('abcdef@'), ('abcdef#'), ('abcdef$'), ('abcdef%'),
                                  ('abcdef^'), ('abcdef&'), ('abcdef%'), ('abcdef*'), ('abcdef('), ('abcdef)'),
                                  ('abcdef-'), ('abcdef+'), ('abcdef=')])
# @pytest.mark.parametrize("name", [('1'), ('aaaaa'), ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')])
def test_js(name):
    driver = webdriver.Chrome()
    driver.get("https://koshelek.ru/authorization/signup")
    time.sleep(7)

    shadow_host = driver.find_element(By.TAG_NAME, "section").find_element(By.CLASS_NAME, "remoteComponent")
    shadow_root = shadow_host.shadow_root
    shadow_contents = shadow_root.find_elements(By.CSS_SELECTOR, 'input')
    shadow_contents[0].send_keys(f'{name}')
    shadow_contents[1].click()

    shadow_host = driver.find_element(By.TAG_NAME, "section").find_element(By.CLASS_NAME, "remoteComponent")
    shadow_root = shadow_host.shadow_root
    assert shadow_root.find_elements(By.CSS_SELECTOR, 'span')[3].text == 'Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы'

    # time.sleep(5)
    driver.quit()


