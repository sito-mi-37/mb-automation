from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from datetime import date
import time


class PaymentProviderListPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    CREATE_PAYMENT_PROVIDER = "//a[normalize-space()='Create Payment Provider']"
    