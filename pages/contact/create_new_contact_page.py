from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils
import time

class CreateNewContact(BaseDriver):
    log = Utils.custom_logger()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    FIRST_NAME_FIELD = "//input[@id='first_name']"
    LAST_NAME_FIELD = "//input[@id='surname']"
    COMMUNICATION_TAB_BUTTON = "//span[contains(text(),'Communication')]"
    EMAIL_ADDRESS_FIELD = "//input[@id='email_address']"
    CREATE_CONTACT_BUTTON = "//span[normalize-space()='Create Contact']"
    CANCEL_CONTACT_CREATION_BUTTON = "//a[normalize-space()='Cancel']"
    TOAST_MESSAGE = "57NNUr9IP"

    def get_first_name_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.FIRST_NAME_FIELD)

    def get_last_name_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.LAST_NAME_FIELD)

    def get_communication_tab(self):
        return self.driver.find_element(By.XPATH, self.COMMUNICATION_TAB_BUTTON)

    def get_email_address_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.EMAIL_ADDRESS_FIELD)

    def get_create_contact_button(self):
        return  self.driver.find_element(By.XPATH, self.CREATE_CONTACT_BUTTON)

    def get_cancel_contact_creation_button(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CANCEL_CONTACT_CREATION_BUTTON)

    def get_toast_message(self):
        return self.wait_for_visibility_of_element_located(By.ID, self.TOAST_MESSAGE)

    def fill_out_required_fields(self, firstname, surname, email):
        self.log.info("Filling out required contact fields")
        self.get_first_name_field().send_keys(firstname)
        time.sleep(2)
        self.get_last_name_field().send_keys(surname)
        time.sleep(2)
        # click on communications tab
        self.get_communication_tab().click()
        time.sleep(3)
        self.get_email_address_field().send_keys(email)

    def click_submit(self):
        # click on submit button
        self.log.info("Submitting form")
        self.get_create_contact_button().click()

    def create_a_new_contact(self, firstname, surname, email):
        self.fill_out_required_fields(firstname, surname, email)
        self.click_submit()
        # assert "created" in self.get_toast_message().text

