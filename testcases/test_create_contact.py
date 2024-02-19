import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.contact.contacts_page import ContactPage
from pages.contact.create_new_contact_page import CreateNewContact
from pages.dashboard_page import DashboardPage


@pytest.mark.usefixtures("setup")
class TestCreateContact():
    def test_create_contact(self):

        # click contact module
        dp = DashboardPage(self.driver)
        dp.contact_click()

        time.sleep(4)

        # open contact form "create contact"
        cp = ContactPage(self.driver)
        cp.click_create_contact()

        # fill out required fields  (firstname, lastname, email)
        cncp = CreateNewContact(self.driver)
        cncp.fill_out_required_fields("sito", "deBill", "sb@gmail.com")


        time.sleep(3)

        # click on create contact button
        cncp.click_submit()

        time.sleep(4)




