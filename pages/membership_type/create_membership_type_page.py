from selenium.webdriver import ActionChains
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
    PRICE_START_DATE = f"//input[@placeholder='{date.today()}']"
    PRICE_AMOUNT_FIELD = "//input[@id='renewal_amount']"
    SET_PRICE_SUBMIT = "//button[@type='submit']"

    C_MONTH_YEAR = "//div[@class='vc-title vc-text-lg vc-text-gray-800 vc-font-semibold hover:vc-opacity-75']"
   
    NEXT_BUTTON = "(//*[name()='svg'])[15]"


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
        return self.wait_for_visibility_of_element_located(By.XPATH, self.PRICE_START_DATE)
    
    def get_price_amount_field(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.PRICE_AMOUNT_FIELD)
    
    def get_set_price_submit(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.SET_PRICE_SUBMIT)
    
    def get_c_month_year(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.C_MONTH_YEAR)
    
    def get_next_button(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.NEXT_BUTTON)


    def create_rolling_membership_type(self, customer_type, membership_type_name, duration, grace_period, renewal_due_date, amount):
        time.sleep(2)
        self.select_by_visible_text(customer_type, self.get_customer_type_field())
        self.get_membership_type_name_field().send_keys(membership_type_name)
        self.get_duration_field().send_keys(duration)
        self.get_grace_period_field().send_keys(grace_period)
        self.scroll_to_element(self.get_duration_field())
        # manually select Rolling renewal option.
        self.get_renewal_type().click()
        self.wait_for_visibility_of_element_located(By.XPATH, "//option[normalize-space()='Rolling']").click()
        self.get_renewal_due_period_field().send_keys(renewal_due_date)
        self.get_publish_checkbox().click()
        self.get_submit_button().click()
        time.sleep(3)
        self.get_set_price_button().click()
        # select  date
        self.hover_over_element(self.get_price_start_date_field())
        
        month_year = self.get_c_month_year().text
        print(month_year)
        if month_year != "June 2024":
            #  check if month_year is not June 2024
             while month_year != "June 2024":
                self.get_next_button().click()
                time.sleep(2)   
        time.sleep(4)                                  
        self.wait_for_element_to_be_clickable(By.XPATH, "//span[@aria-label='Wednesday, June 19, 2024']").click()
        print(date.today().strftime("%A, %B %d, %Y"))
        # self.get_price_start_date_field().send_keys("2024-06-19")
        self.get_price_amount_field().send_keys(amount)
        time.sleep(2)
        self.get_set_price_submit().click()
        time.sleep(5)
        