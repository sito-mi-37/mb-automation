from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
import time


class DashboardPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    DASHBOARD = "//span[@class='text-white sidebar-label']"
    CONTACT_MODULE_BUTTON = "//a[normalize-space()='Contacts']"
    ORGANISATION_MODULE_BUTTON = "//a[normalize-space()='Organisations']"
    MEMBERSHIP_TYPE_BUTTON = "//a[normalize-space()='Membership Types']"
    ADMINS_MODULE_BUTTON = "//a[normalize-space()='Admins']"


    def click_dashboard_button(self):
        element = self.wait_for_element_to_be_clickable(By.XPATH, self.DASHBOARD)
        element.click()

    def get_contact_module_button(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CONTACT_MODULE_BUTTON)

    def get_organisation_module_button(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.ORGANISATION_MODULE_BUTTON)

    def get_membership_type_module(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.MEMBERSHIP_TYPE_BUTTON)
    
    def get_admins_module_button(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.ADMINS_MODULE_BUTTON)

    def contact_click(self):
        self.get_contact_module_button().click()

    def organisation_click(self):
        self.get_organisation_module_button().click()

    def membership_type_click(self):
        self.get_membership_type_module().click()

    def admins_click(self):
        self.get_admins_module_button().click()

    def reset_dashboard(self):
        self.scroll_to_page_top()
        self.click_dashboard_button()
        time.sleep(2)


