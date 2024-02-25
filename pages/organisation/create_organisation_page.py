import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class CreateOrgPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    CREATE_ORGANISATION_BUTTON = "//a[normalize-space()='Create Organisation']"
    ORGANISATION_NAME_FIELD = "//input[@id='name']"
    FULL_NAME_FIELD = "//input[@id='full_name']"
    COMMUNICATION_TAB = "//span[contains(text(),'Communication')]"
    ORGANISATION_INFO = "//span[contains(text(),'Organisation Info')]"
    EMAIL_FIELD = "//input[@id='email_address']"
    CREATE_ORG_SUBMIT = "//button[@type='submit']"
    CREATE_ANOTHER_BUTTON = "//span[normalize-space()='Create & Add Another']"
    CANCEL = "//a[normalize-space()='Cancel']"


    def get_create_organisation_button(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CREATE_ORGANISATION_BUTTON)

    def get_create_organisation_name_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.ORGANISATION_NAME_FIELD)

    def get_fullname_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.FULL_NAME_FIELD)

    def get_communication_tab(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.COMMUNICATION_TAB)

    def get_organisation_info(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.ORGANISATION_INFO)

    def get_email_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.EMAIL_FIELD)

    def get_create_org_submit(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CREATE_ORG_SUBMIT)

    def get_create_another_button(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CREATE_ANOTHER_BUTTON)

    def get_cancel(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CANCEL)

    def create_new_org(self, org_name1, fullname1, email1, org_name2, fullname2, email2):
        self.get_create_organisation_button().click()
        self.get_create_organisation_name_field().send_keys(org_name1)
        self.get_fullname_field().send_keys(fullname1)
        self.get_communication_tab().click()
        self.get_email_field().send_keys(email1)
        self.get_create_another_button().click()
        time.sleep(3)
        self.get_email_field().send_keys(email2)
        self.get_organisation_info().click()
        self.get_create_organisation_name_field().send_keys(org_name2)
        self.get_fullname_field().send_keys(fullname2)
        self.get_create_org_submit().click()
        time.sleep(2)

