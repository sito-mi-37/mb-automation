import time
from parameterized import parameterized
import pytest
import os
from utilities.read_file_data import read_excel_data, read_csv_data
from ddt import data, unpack, ddt
from pages.contact.contacts_list_page import ContactPage
from pages.contact.create_new_contact_page import CreateNewContact
from pages.dashboard.dashboard_page import DashboardPage
from pages.organisation.create_organisation_page import CreateOrgPage
from pages.organisation.organisation_list_page import OrganisationListPage
from pages.membership_type.membership_list_page import MembershipListPage
from pages.membership_type.create_membership_type_page import CreateMembershipPage



@pytest.mark.usefixtures("setup")
@ddt
class TestCreateContact:

    filepath = os.path.join("..","testdata","contact")
    # -------------------------- CONTACTS TEST CASES -------------------------------
    # def test_create_contact(self):
    #     dp = DashboardPage(self.driver)
    #     dp.contact_click()
    #     time.sleep(4)
    #     cp = ContactPage(self.driver)
    #     cp.click_create_contact()
    #     cncp = CreateNewContact(self.driver)
    #     cncp.create_a_new_contact("lito", "dill", "ld@gmail.com")
    #     time.sleep(4)
    #     assert "Contact Details" in self.driver.title
    #     # time.sleep(3)

    # @pytest.mark.parametrize("firstname, surname, email", read_csv_data("testdata\data.csv"))
    # def test_quick_create_contact(self, firstname, surname, email):
    #     dp = DashboardPage(self.driver)
    #     dp.reset_dashboard()
    #     dp.contact_click()
    #     time.sleep(4)
    #     expected_title = "Contacts"
    #     clp = ContactPage(self.driver)
    #     clp.create_quick_contact(firstname=firstname, surname=surname, email=email)
    #     assert expected_title in self.driver.title

    # #     confirm you locate the created contact

    # # --------------------------- ORGANISATION TEST CASES --------------------------------------
    # def test_create_organisation(self):
    #     dp = DashboardPage(self.driver)
    #     dp.reset_dashboard()
    #     dp.organisation_click()
    #     cop = CreateOrgPage(self.driver)
    #     cop.create_new_org("Org Test1", "matt page", "otmp@co.uk", "Org test2", "Dave hun", "otdh@co.uk")
    #     # assert "Organisation Details" in self.driver.title

    # def test_quick_create_organisation(self):
    #     dp = DashboardPage(self.driver)
    #     dp.reset_dashboard()
    #     dp.organisation_click()
    #     time.sleep(3)
    #     olp = OrganisationListPage(self.driver)
    #     olp.create_quick_organisation("Man-United", "090434553", "manu@co.uk")

    @pytest.mark.parametrize("customer_type, membership_type_name, duration, grace_period, renewal_type, renewal_due_date", read_csv_data("testdata\membership_type_data.csv"))
    def test_create_rolling_membership_type(self, customer_type, membership_type_name, duration, grace_period, renewal_type, renewal_due_date):
        dp = DashboardPage(self.driver)
        dp.reset_dashboard() 
        dp.scroll_to_element(dp.get_admins_module_button())
        dp.membership_type_click()
        time.sleep(3)
        mlp = MembershipListPage(self.driver)
        mlp.get_create_membership_type_button().click()
        cm = CreateMembershipPage(self.driver)
        cm.create_membership_type(customer_type, membership_type_name, duration, grace_period, renewal_type, renewal_due_date)
        


