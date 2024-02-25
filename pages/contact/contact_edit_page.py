from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class ContactEditPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    DESCRIPTION_TEXT_AREA = "//trix-editor[@placeholder='Description']"
    UPDATE_CONTACT_BUTTON = "//span[normalize-space()='Update Contact']"
    COMMUNICATION_TAB = "//div[@class='py-5 px-8 border-b-2 focus:outline-none tab cursor-pointer flex items-center text-grey-black font-bold border-primary']"
    EMAIL_ADDRESS_2_FIELD = "//input[@id='email_address_2']"

    def get_description_text_area(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.DESCRIPTION_TEXT_AREA)

    def get_update_contact_button(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.UPDATE_CONTACT_BUTTON)

    def get_communication_tab(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.COMMUNICATION_TAB)

    def get_email_address_2_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.EMAIL_ADDRESS_2_FIELD)