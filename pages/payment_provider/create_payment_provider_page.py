from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from datetime import date
import time


class CreatePaymentProviderPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    CPP_NAME_FIELD = "//input[@id='name']"
    CPP_PAYMENT_METHOD_SELECT_FIELD = "//select[@id='payment_method']"
    CPP_SUBMIT_BUTTON = "//button[@type='submit']"

    def get_cpp_name_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CPP_NAME_FIELD)
    
    def get_cpp_payment_method_select_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CPP_PAYMENT_METHOD_SELECT_FIELD)
    
    def get_cpp_submit_button(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CPP_SUBMIT_BUTTON)
    
    
    def create_payment_provider(self, name, payment_method):
        self.get_cpp_name_field().send_keys(name)
        self.select_by_visible_text(payment_method, self.get_cpp_payment_method_select_field())
        self.get_cpp_submit_button().click()