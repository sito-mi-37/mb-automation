import time
import pytest
import os
from utilities.read_file_data import read_csv_data
from ddt import data, unpack, ddt
from pages.contact.create_new_contact_page import CreateNewContact
from pages.dashboard.dashboard_page import DashboardPage
from pages.organisation.create_organisation_page import CreateOrgPage
from pages.organisation.organisation_list_page import OrganisationListPage
from pages.membership_type.membership_list_page import MembershipListPage
from pages.membership_type.create_membership_type_page import CreateMembershipPage
from pages.contact.contact_detail_page import ContactDetailPage
from pages.contact.contacts_list_page import ContactPage


@pytest.mark.usefixtures("setup")
@ddt
class TestMemberbase:

    filepath = os.path.join("..","testdata","contact")
    # -------------------------- CONTACTS TEST CASES -------------------------------
    @pytest.mark.parametrize("name, surname, email", read_csv_data("testdata\contacts_data.csv"))
    def test_create_contact(self, name, surname, email):
        dp = DashboardPage(self.driver)
        dp.contact_click()
        time.sleep(4)
        cp = ContactPage(self.driver)
        cp.click_create_contact()
        cncp = CreateNewContact(self.driver)
        cncp.create_a_new_contact(name, surname, email)
        time.sleep(4)

        title = self.driver.title
        print(title)
        # assert "Contact Details" in self.driver.title
        # time.sleep(3)
