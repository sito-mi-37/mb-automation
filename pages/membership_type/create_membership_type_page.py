from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from datetime import date
import time


class CreateMembershipPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    CUSTOMER_TYPE_FIELD = "//select[@id='customer_type']"
    MEMBERSHIP_TYPE_NAME = "//input[@id='name']"
    DURATION_FIELD = "//input[@id='duration']"
    GRACE_PERIOD_FIELD = "//input[@id='grace_period_days']"
    RENEWAL_TYPE = "renewal_type"
    RENEWAL_DUE_PERIOD_FIELD = "//input[@id='renewal_reminder_days']"
    PUBLISH_CHECKBOX = "//input[@id='published']"
    SUBMIT_BUTTON = "//button[@type='submit']"
    SET_PRICE_BUTTON = "//div[@id='Set Price']"
    PRICE_START_DATE = f"//input[@placeholder={date.today()}]"
    PRICE_AMOUNT_FIELD = "//input[@id='renewal_amount']"
    SET_PRICE_SUBMIT = "//button[@type='submit']"




    def get_customer_type_field(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CUSTOMER_TYPE_FIELD)
     
    def get_membership_type_name_field(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.MEMBERSHIP_TYPE_NAME)

    def get_duration_field(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.DURATION_FIELD)
    
    def get_grace_period_field(self): 
        return self.wait_for_element_to_be_clickable(By.XPATH, self.GRACE_PERIOD_FIELD)
    
    def get_renewal_type(self):
        return self.wait_for_element_to_be_clickable(By.ID, self.RENEWAL_TYPE)
    
    def get_renewal_due_period_field(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.RENEWAL_DUE_PERIOD_FIELD)
    
    def get_publish_checkbox(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.PUBLISH_CHECKBOX)
    
    def get_submit_button(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.SUBMIT_BUTTON)

    def get_set_price_button(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.SET_PRICE_BUTTON)
    
    def get_price_start_date_field(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.PRICE_START_DATE)
    
    def get_price_amount_field(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.PRICE_AMOUNT_FIELD)
    
    def get_set_price_submit(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.SET_PRICE_SUBMIT)
    

    def create_membership_type(self, customer_type, membership_type_name, duration, grace_period, renewal_type, renewal_due_date):
        time.sleep(2)
        self.select_by_visible_text(customer_type, self.get_customer_type_field())
        self.get_membership_type_name_field().send_keys(membership_type_name)
        self.get_duration_field().send_keys(duration)
        self.get_grace_period_field().send_keys(grace_period)
        self.scroll_to_element(self.get_duration_field())
        # self.select_by_index(renewal_type, self.get_renewal_type())
        # manually select Rolling renewal option.
        self.get_renewal_type().click()
        self.wait_for_visibility_of_element_located(By.XPATH, "//option[normalize-space()='Rolling']").click()
        self.get_renewal_due_period_field().send_keys(renewal_due_date)
        self.get_publish_checkbox().click()
        self.get_submit_button().click()
        time.sleep(3)