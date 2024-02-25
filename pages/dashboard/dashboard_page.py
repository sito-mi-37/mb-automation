from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class DashboardPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    CONTACT_MODULE_BUTTON = "//a[normalize-space()='Contacts']"
    ORGANISATION_MODULE_BUTTON = "//a[normalize-space()='Organisations']"

    def get_contact_module_button(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CONTACT_MODULE_BUTTON)


    def get_organisation_module_button(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.ORGANISATION_MODULE_BUTTON)

    def contact_click(self):
        self.get_contact_module_button().click()

    def organisation_click(self):
        self.get_organisation_module_button().click()