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


    def get_view_contact_button(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.VIEW_CONTACT_BUTTON)
    def click_create_contact(self):
        self.wait_for_element_to_be_clickable(By.XPATH, self.CREATE_CONTACT_BUTTON).click()

    def get_edit_contact_button(self):
        self.wait_for_visibility_of_element_located(By.XPATH, self.EDIT_CONTACT_BUTTON)
