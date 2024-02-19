from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_driver import BaseDriver


class DashboardPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def contact_click(self):
        self.wait_for_element_to_be_clickable(By.XPATH, "//a[normalize-space()='Contacts']").click()
