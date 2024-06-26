import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class OrganisationEditPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    COMPANY_NUMBER = "//input[@id='company_number']"
    UPDATE_ORG_SUBMIT_BUTTON = "//button[@type='submit']"
    DESCRIPTION_FIELD = "//trix-editor[@placeholder='Description']"
    WEBSITE = "//input[@id='website']"
    EMAIL = "//input[@id='email_address']"
    MAIN_TELEPHONE = "(//input[@id='telephone_1'])[1]"
    OTHER_TELEPHONE = "(//input[@id='telephone_2'])[1]"
    COMMUNICATION_TAB = "//span[contains(text(),'Communication')]"


    def get_company_number_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.COMPANY_NUMBER)

    def get_update_org_submit_btn(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.UPDATE_ORG_SUBMIT_BUTTON)

    def get_description_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.DESCRIPTION_FIELD)
    
    def get_website_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.WEBSITE)

    def get_communication_tab(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.COMMUNICATION_TAB)

    def get_email_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.EMAIL)

    def get_main_telephone_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.MAIN_TELEPHONE)

    def get_other_telephone_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.OTHER_TELEPHONE)
    
    def update_organisation(self, company_number, description, website,email, main_telephone, other_telephone):
        self.get_description_field().send_keys(description)
        self.get_company_number_field().send_keys(company_number)
        self.get_website_field().send_keys(website)
        self.get_communication_tab().click()
        time.sleep(4)
        self.get_email_field().clear()
        self.get_email_field().send_keys(email)
        self.get_main_telephone_field().send_keys(main_telephone)
        self.get_other_telephone_field().send_keys(other_telephone)
        time.sleep(2)
        self.get_update_org_submit_btn().click()
        time.sleep(4)




