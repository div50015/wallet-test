import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class RegistrationPage:
    SHADOW_HOST_FIELD = (By.CLASS_NAME, "remoteComponent")
    SHADOW_FORM_FILED = (By.CSS_SELECTOR, 'form')
    SHADOW_DIV_NAME = (By.XPATH, ".//div[@data-wi='user-name']")
    SHADOW_DIV_EMAIL = (By.XPATH, ".//div[@data-wi='identificator']")
    SHADOW_DIV_PASSWORD = (By.XPATH, ".//div[@data-wi='password']")
    SHADOW_DIV_REF_CODE = (By.XPATH, ".//div[@data-wi='referral']")
    SHADOW_DIV_CHECKBOX = (By.XPATH, ".//div[@data-wi='user-agreement']")
    SHADOW_DIV_BUTTON = (By.XPATH, ".//div[@data-wi='submit-button']")
    SHADOW_INPUT_NAME = (By.CSS_SELECTOR, "input")
    SHADOW_INPUT_EMAIL = (By.CSS_SELECTOR, "input")
    SHADOW_INPUT_PASSWORD = (By.CSS_SELECTOR, "input")
    SHADOW_INPUT_REF_CODE = (By.CSS_SELECTOR, "input")
    SHADOW_BUTTON = (By.CSS_SELECTOR, "button")
    SHADOW_SPAN_NAME = (By.XPATH, ".//span[@class='k-text']")
    SHADOW_SPAN_EMAIL = (By.XPATH, ".//span[@class='k-text']")
    SHADOW_SPAN_PASSWORD = (By.XPATH, ".//span[@class='k-text']")
    SHADOW_SPAN_REF_CODE = (By.XPATH, ".//span[@class='k-text']")
    SHADOW_SPAN_CHECKBOX = (By.XPATH, ".//div")

    def __init__(self, driver):
        self.driver = driver

    def shadow_form(self):
        return self.driver.find_element(*self.SHADOW_HOST_FIELD).shadow_root.find_element(*self.SHADOW_FORM_FILED)

    # def find_element_css(self, webdriver, teg):
    #     return  webdriver.find_element(By.CSS_SELECTOR, teg)
    #
    # def find_element_xpath(self, webdriver, teg):
    #     return  webdriver.find_element(By.XPATH, teg)
    #
    # def shadow_div_name(self):
    #     return self.shadow_form().find_element(*self.SHADOW_DIV_NAME)
    #
    def shadow_input_name(self, name):
        return self.shadow_form().find_element(*self.SHADOW_DIV_NAME).find_element(*self.SHADOW_INPUT_NAME).send_keys(name)

    def shadow_input_email(self, email):
        return self.shadow_form().find_element(*self.SHADOW_DIV_EMAIL).find_element(*self.SHADOW_INPUT_EMAIL).send_keys(email)

    def shadow_input_password(self, password):
        return self.shadow_form().find_element(*self.SHADOW_DIV_PASSWORD).find_element(*self.SHADOW_INPUT_PASSWORD).send_keys(password)

    def shadow_input_ref_code(self, code):
        return self.shadow_form().find_element(*self.SHADOW_DIV_REF_CODE).find_element(*self.SHADOW_INPUT_REF_CODE).send_keys(code)

    def shadow_input_char_name(self, char):
        return self.shadow_form().find_element(*self.SHADOW_DIV_NAME).find_element(*self.SHADOW_INPUT_NAME).send_keys(f'Name{char}')

    def shadow_span_name(self):
        return self.shadow_form().find_element(*self.SHADOW_DIV_NAME).find_element(*self.SHADOW_SPAN_NAME)

    def shadow_span_email(self):
        return self.shadow_form().find_element(*self.SHADOW_DIV_EMAIL).find_element(*self.SHADOW_SPAN_EMAIL)

    def shadow_span_password(self):
        return self.shadow_form().find_element(*self.SHADOW_DIV_PASSWORD).find_element(*self.SHADOW_SPAN_PASSWORD)

    def shadow_span_ref_code(self):
        return self.shadow_form().find_element(*self.SHADOW_DIV_REF_CODE).find_element(*self.SHADOW_SPAN_REF_CODE)

    def shadow_span_checkbox(self):
        return self.shadow_form().find_element(*self.SHADOW_DIV_CHECKBOX).find_element(*self.SHADOW_SPAN_CHECKBOX)

    def shadow_next_button(self):
        return self.shadow_form().find_element(*self.SHADOW_DIV_BUTTON).find_element(*self.SHADOW_BUTTON)




