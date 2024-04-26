from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


def test_js():
    driver = webdriver.Chrome()
    driver.get("https://koshelek.ru/authorization/signup")
    time.sleep(5)

    # error cod
    shadow_host = driver.find_element(By.TAG_NAME, "section").find_element(By.CLASS_NAME, "remoteComponent")
    shadow_root = shadow_host.shadow_root
    shadow_content1 = shadow_root.find_element(By.CSS_SELECTOR, 'input').send_keys('1')
    shadow_content2 = shadow_root.find_elements(By.CSS_SELECTOR, 'input')[1].click()

    shadow_host1 = driver.find_element(By.TAG_NAME, "section").find_element(By.CLASS_NAME, "remoteComponent")
    shadow_root1 = shadow_host.shadow_root
    shadow_content11 = shadow_root.find_elements(By.CSS_SELECTOR, 'span')[21].text()
    print(f'\r\ntype cont11 = {shadow_content11}')

    # shadow_text1 = shadow_root.find_element(By.XPATH(".//span[contains(text(),' Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы ')]"))

    time.sleep(5)
    # print(f'\r\ntype host = {type(shadow_host)}')
    # print(f'type root = {type(shadow_root)}')
    # print(f'type cont = {type(shadow_content1)}')
    # print(f'cont = {shadow_content1}')
    driver.quit()

    # work cod
    # shadow_host = driver.find_element(By.CSS_SELECTOR, ".remoteComponent")
    # shadow_root = shadow_host.shadow_root
    # shadow_content = shadow_root.find_element(By.CSS_SELECTOR, 'input')

    # js script
    # shadow_host = driver.find_element(By.CSS_SELECTOR, '.remoteComponent')
    # print(F'\r\ntype = {type(shadow_host)}')
    # print(F'\r\nlist = {shadow_host}')
    # children = driver.execute_script('return arguments[0].shadowRoot.children', shadow_host)
    # print(F'\r\ntype = {type(children)}')
    # print(F'\r\nlist = {children}')
    # # shadow_content = next(child for child in children if child.get_attribute('id') == 'input')
    # shadow_content = children[0]
    # print(F'\r\ntype = {type(shadow_content)}')
    # print(F'\r\nlist = {shadow_content}')
    # shadow_content.find_element(By.TAG_NAME, 'input')

    driver.quit()


