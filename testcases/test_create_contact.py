import time
import pytest
from selenium.webdriver.common.by import By

from pages.contact.contact_detail_page import ContactDetailPage
from pages.contact.contact_edit_page import ContactEditPage
from pages.contact.contacts_page import ContactPage
from pages.contact.create_new_contact_page import CreateNewContact
from pages.dashboard.dashboard_page import DashboardPage
from pages.organisation.create_organisation_page import CreateOrgPage
from pages.organisation.organisation_detail_page import OrganisationDetailsPage
from pages.organisation.organisation_edit_page import OrganisationEditPage
from pages.organisation.organisation_list_page import OrganisationListPage


@pytest.mark.usefixtures("setup")
class TestCreateContact:
    # -------------------------- CONTACTS TEST CASES -------------------------------
    def test_create_contact(self):
        dp = DashboardPage(self.driver)
        dp.contact_click()
        time.sleep(4)
        cp = ContactPage(self.driver)
        cp.click_create_contact()
        cncp = CreateNewContact(self.driver)
        cncp.create_a_new_contact("lito", "dill", "ld@gmail.com")
        time.sleep(4)
        assert self.driver.find_element(By.XPATH, "//span[contains(text(),'Details')]")
        time.sleep(3)

    def test_create_contact_with_missing_required_field(self):
        dp = DashboardPage(self.driver)
        dp.contact_click()
        time.sleep(3)
        cp = ContactPage(self.driver)
        actual_url = f"https://world-health-organisation.memberbase-test.com/crm/resources/contacts"
        cp.click_create_contact()
        cncp = CreateNewContact(self.driver)
        cncp.create_a_new_contact("lito", "dill", "")
        cncp.get_cancel_contact_creation_button().click()
        self.driver.switch_to.alert.accept()
        time.sleep(3)
        expected_url = self.driver.current_url
        assert actual_url == expected_url

    def test_view_all_contacts_details(self):
        dp = DashboardPage(self.driver)
        dp.contact_click()
        time.sleep(3)
        cp = ContactPage(self.driver)
        cp.get_view_contact_button().click()
        cdp = ContactDetailPage(self.driver)
        cdp.view_tab_details()
        dp.return_to_dashboard()

    def test_add_address(self):
        dp = DashboardPage(self.driver)
        dp.contact_click()
        time.sleep(4)
        cp = ContactPage(self.driver)
        cp.get_view_contact_button().click()
        cdp = ContactDetailPage(self.driver)
        cdp.get_manage_contact_dropdown().click()
        time.sleep(2)
        cdp.get_add_address_button().click()
        cdp.get_address_field().send_keys("Rumuokoro phase 12")
        cdp.select_by_visible_text("Nigeria", cdp.get_country_select())
        cdp.get_save_address_button().click()
        cdp.scroll_to_element(cdp.get_addresses_table())

    # def test_document_upload(self):
    #     dp = DashboardPage(self.driver)
    #     dp.contact_click()
    #
    #     time.sleep(4)
    #     cp = ContactPage(self.driver)
    #     cp.get_view_contact_button().click()
    #
    #     cdp = ContactDetailPage(self.driver)
    #     cdp.get_manage_contact_dropdown().click()
    #     time.sleep(2)
    #
    #     cdp.get_upload_document_button().click()
    #     cdp.get_upload_document_input().send_keys("../../testdata/sa.png")
    #     cdp.get_add_document_description().send_keys("major flow smartcat")
    #
    #     cdp.get_ad_save_document_button().click()
    #     time.sleep(3)

    def test_add_notes(self):
        dp = DashboardPage(self.driver)
        dp.contact_click()
        time.sleep(4)
        cp = ContactPage(self.driver)
        cp.get_view_contact_button().click()
        cdp = ContactDetailPage(self.driver)
        cdp.add_new_note("Thanks for your gifts")

    # def test_add_employment(self):
    #     pass
    #
    def test_change_bus_unit(self):
        dp = DashboardPage(self.driver)
        dp.contact_click()
        time.sleep(2)
        cp = ContactPage(self.driver)
        cp.get_view_contact_button().click()
        time.sleep(2)
        cdp = ContactDetailPage(self.driver)
        cdp.change_business_unit("World Health Organisation")

    # --------------------------- ORGANISATION TEST CASES --------------------------------------

    def test_create_organisation(self):
        dp = DashboardPage(self.driver)
        dp.organisation_click()
        cop = CreateOrgPage(self.driver)
        cop.create_new_org("Org Test1", "matt page", "otmp@co.uk", "Org test2", "Dave hun", "otdh@co.uk")

    def test_view_organisation(self):
        dp = DashboardPage(self.driver)
        dp.organisation_click()
        olp = OrganisationListPage(self.driver)
        olp.get_view_organisation_button().click()
        odp = OrganisationDetailsPage(self.driver)
        odp.view_org_details()
        odp.return_to_dashboard()
        time.sleep(4)

    def test_update_organisation(self):
        dp = DashboardPage(self.driver)
        dp.organisation_click()
        olp = OrganisationListPage(self.driver)
        olp.get_edit_organisation_button().click()
        oep = OrganisationEditPage(self.driver)
        oep.update_org("090567483")

