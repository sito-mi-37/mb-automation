import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class OrganisationDetailsPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ADDRESS_AND_COMMUNICATION = "//span[contains(text(),'Addresses & Communication')]"
    MEMBERSHIP = "//span[@class='tab-title inline-flex items-center']//span[contains(text(),'Membership')]"
    SUBSCRIPTIONS = "//span[@class='tab-title inline-flex items-center']//span[contains(text(),'Membership')]"
    FINANCE = "//span[contains(text(),'Finance')]"
    COMMUNICATION = "//button[@dusk='communication-tab']//span[contains(text(),'Communication')]"
    NOTES = "//span[contains(text(),'Notes')]"
    INTERACTIONS = "//span[contains(text(),'Interactions')]"
    MEMBERS = "//button[@dusk='members-tab']//span[contains(text(),'Members')]"


    def get_address_and_communication(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.ADDRESS_AND_COMMUNICATION)

    def get_membership(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.MEMBERSHIP)

    def get_subscriptions(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.SUBSCRIPTIONS)

    def get_finance(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.FINANCE)

    def get_communication(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.COMMUNICATION)

    def get_notes(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.NOTES)

    def get_interactions(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.INTERACTIONS)

    def get_members(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.MEMBERS)

    def view_org_details(self):
        self.get_address_and_communication().click()
        time.sleep(2)
        self.get_membership().click()
        time.sleep(2)
        self.get_subscriptions().click()
        time.sleep(2)
        self.get_finance().click()
        time.sleep(2)
        self.get_communication().click()
        time.sleep(2)
        self.get_notes().click()
        time.sleep(2)
        self.get_interactions().click()
        time.sleep(2)
        self.get_members().click()







