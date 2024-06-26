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
from pages.contact.contacts_list_page import ContactListPage
from pages.contact.contact_edit_page import ContactEditPage
from pages.organisation.organisation_edit_page import OrganisationEditPage
from pages.groups.group_list_page import GroupListPage


@pytest.mark.usefixtures("setup")
@ddt
class TestMemberbase:

    filepath = os.path.join("..","testdata","contact")
    # -------------------------- CONTACTS TEST CASES -------------------------------
    # @pytest.mark.test
    @pytest.mark.smoke
    @pytest.mark.parametrize("name, surname, email", read_csv_data("testdata\contacts_data.csv"))
    def test_create_contact(self, name, surname, email):
        dp = DashboardPage(self.driver)
        dp.contact_click()
        time.sleep(4)
        cp = ContactListPage(self.driver)
        cp.click_create_contact()
        cncp = CreateNewContact(self.driver)
        cncp.create_a_new_contact(name, surname, email)
        time.sleep(4)

    def test_update_contact(self):
        dp = DashboardPage(self.driver)
        dp.contact_click()
        time.sleep(2)
        clp = ContactListPage(self.driver)
        clp.get_search_input().send_keys("nelson.akujiobi@senior.co.uk")
        time.sleep(4)
        clp.get_edit_first_contact_button().click()
        time.sleep(2)
        cep = ContactEditPage(self.driver)
        cep.update_contact_information("Mr","sito23@yopmail.com", "nelson.akujiobi@senior.co.uk", "Tech enthusiast","sito", "090123456789", "08112345679", "Email" )
        time.sleep(2)

    # @pytest.mark.test
    @pytest.mark.smoke
    def test_create_invoice_for_a_contact(self):
        dp = DashboardPage(self.driver)
        dp.reset_dashboard()
        dp.contact_click()
        time.sleep(2)
        clp = ContactListPage(self.driver)
        clp.get_search_input().send_keys("blessing@yopmail.com")
        clp.get_view_first_contact_button().click()
        time.sleep(2)
        cdp = ContactDetailPage(self.driver)
        cdp.create_invoice("Membership product", "Gold", "Zero VAT", "No 46 Spring Brook", "Nottingham", "Nottinghamshire", "East Midlands", "United Kingdom")
        
    # @pytest.mark.test
    @pytest.mark.smoke
    def test_record_payment(self):
        dp = DashboardPage(self.driver)
        dp.reset_dashboard()
        dp.contact_click()
        time.sleep(2)
        clp = ContactListPage(self.driver)
        clp.get_search_input().send_keys("sito23@yopmail.com")
        time.sleep(2)
        clp.get_view_first_contact_button().click()
        time.sleep(2)
        cdp = ContactDetailPage(self.driver)
        cdp.record_payment("1000", "Bank Transfer", "This is a test ")
        time.sleep(2)

    # retest this because the test passed but the invoice was not settled
    # @pytest.mark.test
    @pytest.mark.smoke
    def test_settling_an_invoice_by_capturing_a_payment(self):
        dp = DashboardPage(self.driver)
        dp.reset_dashboard()
        dp.contact_click()
        time.sleep(2)
        clp = ContactListPage(self.driver)
        clp.get_search_input().send_keys("sito23@yopmail.com")
        clp.get_view_first_contact_button().click()
        time.sleep(2)
        cdp = ContactDetailPage(self.driver)  
        cdp.settle_an_invoice_by_capturing_a_payment()  

        

    # ---------------------------- ORGANISATION TEST CASES ---------------------------------
    @pytest.mark.smoke
    def test_create_organisation(self):
        dp = DashboardPage(self.driver)
        dp.reset_dashboard()
        dp.organisation_click()
        time.sleep(4)
        ol = OrganisationListPage(self.driver)
        ol.create_quick_organisation("Marple Inc", "4467920183", "marple@marple.co.za")
    
    # @pytest.mark.test
    @pytest.mark.smoke
    def test_update_organisation(self):
        dp = DashboardPage(self.driver)
        dp.reset_dashboard()
        dp.organisation_click()
        time.sleep(4)
        olp = OrganisationListPage(self.driver)
        olp.get_search_input().send_keys("marple@marple.co.za")
        time.sleep(4)
        olp.get_edit_first_organisation_button().click()
        time.sleep(4)
        oep = OrganisationEditPage(self.driver)
        oep.update_organisation("09843234211", "Test Desc", "marple.co.uk", "marple@marple.co.uk", "4423119987", "6784030298")
        time.sleep(4)

    # ---------------------------- GROUP TEST CASES ----------------------------------------

    # @pytest.mark.test
    @pytest.mark.smoke
    def test_create_group_category(self):
        dp = DashboardPage(self.driver)
        dp.reset_dashboard()
        dp.groups_click()
        glp = GroupListPage(self.driver)
        glp.create_group_category("Property Owners", "London Base", "Landlord in London only")
        time.sleep(4)

    # @pytest.mark.test
    @pytest.mark.smoke
    def test_create_group(self):
        dp = DashboardPage(self.driver)
        dp.reset_dashboard()
        dp.groups_click()
        glp = GroupListPage(self.driver)
        glp.create_group("London Landlords", "London Landlords Group","Dynamic")
        time.sleep(4)

    # @pytest.mark.test
    @pytest.mark.smoke
    def test_update_group(self):
        dp = DashboardPage(self.driver)
        dp.reset_dashboard()
        dp.groups_click()
        glp = GroupListPage(self.driver)
        glp.update_group("London Essex Landlords", "London Essex Landlords Group")
        time.sleep(4)


    #  -------------------------- MEMBERSHIP-TYPE TEST CASES -------------------------------
    # @pytest.mark.test
    @pytest.mark.smoke
    @pytest.mark.parametrize("customer_type, membership_type_name, duration, grace_period, renewal_due_date, amount ", read_csv_data("testdata\membership_type_data.csv"))
    def test_create_membership_type(self, customer_type, membership_type_name, duration, grace_period, renewal_due_date, amount):
        dp = DashboardPage(self.driver)
        dp.membership_type_click()
        time.sleep(4)
        ml = MembershipListPage(self.driver)
        ml.click_create_membership_type_button()
        time.sleep(4)
        cm = CreateMembershipPage(self.driver)
        cm.create_rolling_membership_type(customer_type, membership_type_name, duration, grace_period, renewal_due_date, amount)
        time.sleep(2)

    # ----------------------------- ACTIVATE MEMBERSHIP TEST CASES -------------------------------------
    @pytest.mark.smoke
    @pytest.mark.parametrize("membership_type, amount, notes", read_csv_data("testdata\membership_activation_data.csv"))
    def test_active_membership(self, membership_type, amount, notes):
        dp = DashboardPage(self.driver)
        dp.reset_dashboard()
        dp.contact_click()
        clp = ContactListPage(self.driver)
        clp.get_view_first_contact_button().click()
        time.sleep(2)
        cdp = ContactDetailPage(self.driver)
        cdp.activate_sole_membership(membership_type)
        time.sleep(4)
        cdp.credit_customer_invoice(amount, notes)
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        cdp.get_membership_tab().click()
        time.sleep(3)


    @pytest.mark.test
    @pytest.mark.smoke
    def test_cancel_membership(self):
        dp = DashboardPage(self.driver)
        dp.reset_dashboard()
        dp.contact_click()
        time.sleep(3)
        clp = ContactListPage(self.driver)
        clp.get_search_input().send_keys("sito23@yopmail.com")
        clp.get_view_first_contact_button().click()
        time.sleep(2)
        cdp = ContactDetailPage(self.driver) 
        cdp.cancel_contact_membership("Suspend", "Emigrating", "Please keep no feeling unshared")
        time.sleep(2)

    def test_upgrading_and_downgrading_a_membership(self):
        dp = DashboardPage(self.driver)
        dp.reset_dashboard()
        dp.contact_click()
        time.sleep(3)
        clp = ContactListPage(self.driver)
        

    
        
