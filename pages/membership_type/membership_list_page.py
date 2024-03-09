from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class MembershipListPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    MEMBERSHIP_TYPE_BUTTON = "//a[normalize-space()='Create Membership Type']"

    def get_create_membership_type_button(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.MEMBERSHIP_TYPE_BUTTON)
    
