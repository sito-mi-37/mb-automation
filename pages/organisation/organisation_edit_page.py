import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class OrganisationEditPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    COMPANY_NUMBER = "//span[normalize-space()='Update Organisation']"
    UPDATE_ORG_SUBMIT_BUTTON = "//button[@type='submit']"

    def get_contact_number_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.COMPANY_NUMBER)

    def get_update_org_submit_btn(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.UPDATE_ORG_SUBMIT_BUTTON)

    def update_org(self, company_number):
        self.get_contact_number_field().send_keys(company_number)
        time.sleep(2)
        self.get_update_org_submit_btn().click()
        time.sleep(2)




