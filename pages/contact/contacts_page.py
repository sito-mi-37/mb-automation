from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class ContactPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_create_contact(self):
        self.wait_for_element_to_be_clickable(By.XPATH, "//a[normalize-space()='Create Contact']").click()
