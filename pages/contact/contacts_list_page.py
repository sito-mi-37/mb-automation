import time

from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils

class ContactPage(BaseDriver):
    log = Utils.custom_logger()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    VIEW_CONTACT_BUTTON = "//tbody/tr[1]/td[10]/div[1]/span[1]/a[1]//*[name()='svg']"
    CREATE_CONTACT_BUTTON = "//a[normalize-space()='Create Contact']"
    EDIT_CONTACT_BUTTON = "//tbody/tr[1]/td[10]/div[1]/span[2]/a[1]//*[name()='svg']"
    QUICK_CREATE_BUTTON = "//div[contains(text(),'Quick Contact')]"
    FIRSTNAME_FIELD = "//input[@id='firstName']"
    SURNAME_FIELD = "//input[@id='surname']"
    EMAIL_FIELD = "//input[@id='emailAddress']"
    SUBMIT_FIELD = "//button[@type='submit']"
    TABLE_LIST = "//table[@class='table w-full table-default']/tbody/tr"
    SEARCH_INPUT = "//input[@placeholder='Search']"



    def get_view_contact_button(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.VIEW_CONTACT_BUTTON)
    def click_create_contact(self):
        self.wait_for_element_to_be_clickable(By.XPATH, self.CREATE_CONTACT_BUTTON).click()

    def get_edit_contact_button(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.EDIT_CONTACT_BUTTON)

    def get_quick_create_button(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.QUICK_CREATE_BUTTON)

    def get_firstname_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.FIRSTNAME_FIELD)

    def get_surname_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.SURNAME_FIELD)

    def get_email_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.EMAIL_FIELD)

    def get_submit_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.SUBMIT_FIELD)

    def get_table_list(self):
        return self.driver.find_elements(By.XPATH, self.TABLE_LIST)

    def get_search_input(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.SEARCH_INPUT)



    def create_quick_contact(self, firstname, surname, email):
        self.get_quick_create_button().click()
        self.get_firstname_field().send_keys(firstname)
        time.sleep(2)
        self.get_surname_field().send_keys(surname)
        time.sleep(2)
        self.get_email_field().send_keys(email)
        time.sleep(2)
        self.get_submit_field().click()

