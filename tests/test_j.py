from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time



def test_js():
    driver = webdriver.Chrome()
    driver.get("https://koshelek.ru/authorization/signup")
    time.sleep(10)
    #   driver.get("file:///localhost")

    # shadow_host = driver.find_element(By.TAG_NAME, "section").find_element(By.CLASS_NAME, "remoteComponent")
    # shadow_root = shadow_host.shadow_root
    # shadow_content = shadow_root.find_element(By.TAG_NAME, 'input')

    shadow_host = driver.find_element(By.CSS_SELECTOR, ".remoteComponent")
    shadow_root = shadow_host.shadow_root.
    shadow_content = shadow_root.find_element(By.CSS_SELECTOR, 'input')

    driver.quit()


