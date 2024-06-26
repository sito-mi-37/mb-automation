from selenium.webdriver.common.by import By
import time
from base.base_driver import BaseDriver


class ContactEditPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    DESCRIPTION_TEXT_AREA = "//trix-editor[@placeholder='Description']"
    UPDATE_CONTACT_BUTTON = "//span[normalize-space()='Update Contact']"
    COMMUNICATION_TAB = "//span[contains(text(),'Communication')]"
    EMAIL_ADDRESS_FIELD = "//input[@id='email_address']"
    EMAIL_ADDRESS_2_FIELD = "//input[@id='email_address_2']"
    TITLE_FIELD = "//select[@id='salutation']"
    MIDDLE_NAME_FIELD = "//input[@id='middle_name']"
    MOBILE_NUMBER_FIELD = "//input[@id='mobile_number']"
    TELEPHONE_FIELD = "//input[@id='telephone']"
    PREFERRED_COMMUNICATION_FIELD = "//select[@id='preferred_communication_method']"


    def get_description_text_area(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.DESCRIPTION_TEXT_AREA)

    def get_update_contact_button(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.UPDATE_CONTACT_BUTTON)

    def get_communication_tab(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.COMMUNICATION_TAB)

    def get_email_address_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.EMAIL_ADDRESS_FIELD)

    def get_email_address_2_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.EMAIL_ADDRESS_2_FIELD)
    
    def get_title_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.TITLE_FIELD)
    
    def get_middle_name_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.MIDDLE_NAME_FIELD)

    def get_mobile_number_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.MOBILE_NUMBER_FIELD)

    def get_telephone_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.TELEPHONE_FIELD)
    
    def get_preferred_communication_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.PREFERRED_COMMUNICATION_FIELD)

    def update_contact_information(self, title, email, email2, description, middle_name, mobile_number, telephone, preferred_comms):
        self.select_by_visible_text(title, self.get_title_field())
        self.get_middle_name_field().send_keys(middle_name)
        self.scroll_to_element(self.get_description_text_area())
        time.sleep(1)
        self.get_description_text_area().send_keys(description)
        self.get_communication_tab().click()
        time.sleep(2)
        self.get_email_address_field().clear()
        time.sleep(1)
        self.get_email_address_field().send_keys(email)
        time.sleep(1)
        self.get_email_address_2_field().send_keys(email2)
        self.get_mobile_number_field().send_keys(mobile_number)
        self.get_telephone_field().send_keys(telephone)
        time.sleep(1)
        self.select_by_visible_text(preferred_comms, self.get_preferred_communication_field())
        time.sleep(1)
        self.get_update_contact_button().click()
        time.sleep(4)

