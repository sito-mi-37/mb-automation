from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class CreateNewContact(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def fill_out_required_fields(self, firstname, lastname, email):
        first_name = self.wait_for_visibility_of_element_located(By.XPATH, "//input[@id='first_name']")
        first_name.send_keys(firstname)

        last_name = self.wait_for_visibility_of_element_located(By.XPATH, "//input[@id='surname']")
        last_name.send_keys(lastname)

        # click on communications tab
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Communication')]").click()

        self.wait_for_visibility_of_element_located(By.XPATH, "//input[@id='email_address']").send_keys(email)

    def click_submit(self):
        # click on submit button
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Create Contact']").click()
