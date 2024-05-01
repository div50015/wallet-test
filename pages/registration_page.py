import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class RegistrationPage:
    SHADOW_HOST_FIELD = (By.CLASS_NAME, "remoteComponent")
    SHADOW_FORM_FILED = (By.CSS_SELECTOR, 'form')
    SHADOW_DIV_NAME = (By.XPATH, ".//div[@data-wi='user-name']")
    SHADOW_INPUT_NAME = (By.CSS_SELECTOR, "input")
    SHADOW_SPAN_NAME = (By.XPATH, ".//span[@class='k-text']")

    def __init__(self, driver):
        self.driver = driver

    def shadow_form(self):
        return self.driver.find_element(*self.SHADOW_HOST_FIELD).shadow_root.find_element(*self.SHADOW_FORM_FILED)
        # return self.driver.find_element(By.CLASS_NAME, "remoteComponent").shadow_root.find_element(By.CSS_SELECTOR, 'form')

    def find_element_css(self, webdriver, teg):
        return  webdriver.find_element(By.CSS_SELECTOR, teg)

    def find_element_xpath(self, webdriver, teg):
        return  webdriver.find_element(By.XPATH, teg)

    def shadow_div_name(self):
        return self.shadow_form().find_element(*self.SHADOW_DIV_NAME)

    def shadow_input_name(self, name):
        return self.shadow_form().find_element(*self.SHADOW_DIV_NAME).find_element(*self.SHADOW_INPUT_NAME).send_keys(name)

    def shadow_span_name(self):
        return self.shadow_form().find_element(*self.SHADOW_DIV_NAME).find_element(*self.SHADOW_SPAN_NAME)



