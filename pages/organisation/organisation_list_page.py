import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class OrganisationListPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    VIEW_ORGANISATION = "//tbody/tr[1]/td[9]/div[1]/span[1]/a[1]//*[name()='svg']"
    EDIT_ORGANISATION = "//tbody/tr[1]/td[9]/div[1]/span[2]/a[1]//*[name()='svg']"
    QUICK_CREATE = "(//div[@class='text-sm py-2 font-light'])[1]"
    BUSINESS_NAME_FIELD = "//input[@id='name']"
    TELEPHONE_FIELD = "telephone1"
    EMAIL_FIELD = "//input[@id='emailAddress']"
    SUBMIT_BUTTON = "//button[@type='submit']"
    SEARCH_INPUT = "//input[@class='appearance-none form-search w-search pl-search shadow']"

    def get_search_input(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.SEARCH_INPUT)

    def get_view_organisation_button(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.VIEW_ORGANISATION)

    def get_edit_first_organisation_button(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.EDIT_ORGANISATION)

    def get_quick_create(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.QUICK_CREATE)

    def get_business_name_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.BUSINESS_NAME_FIELD)

    def get_telephone_field(self):
        return self.wait_for_element_to_be_clickable(By.ID, self.TELEPHONE_FIELD)

    def get_email_field(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.EMAIL_FIELD)

    def get_submit_button(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.SUBMIT_BUTTON)


    def create_quick_organisation(self, business_name, telephone, email):
        self.get_quick_create().click()
        time.sleep(2)
        self.get_business_name_field().send_keys(business_name)
        time.sleep(2)
        self.get_telephone_field().send_keys(telephone)
        time.sleep(2)
        self.get_email_field().send_keys(email)
        time.sleep(2)
        self.get_submit_button().click()




