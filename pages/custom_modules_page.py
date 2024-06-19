from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class CustomModulePage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

