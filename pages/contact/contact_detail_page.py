import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base.base_driver import BaseDriver


class ContactDetailPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    DETAILS_TAB = "//span[contains(text(),'Details')]"
    EMPLOYMENT_TAB = "//span[@class='tab-title inline-flex items-center']//span[contains(text(),'Employment')]"
    ADDRESS_AND_COMMUNICATION_TAB = "//span[contains(text(),'Addresses & Communication')]"
    MEMBERSHIP_TAB = "//span[@class='tab-title inline-flex items-center']//span[contains(text(),'Membership')]"
    SUBSCRIPTION_TAB = "//span[contains(text(),'Subscriptions')]"
    EVENTS_TAB = "//span[@class='tab-title inline-flex items-center']//span[contains(text(),'Events')]"
    FINANCE_TAB = "//span[contains(text(),'Finance')]"
    DOCUMENTS_TAB = "//span[contains(text(),'Documents')]"
    COMMUNICATION_TAB = "//button[@class='py-5 px-8 border-b-2 focus:outline-none tab text-grey-black font-bold border-primary']//span[contains(text(),'Communication')]"
    NOTES_TAB = "//span[contains(text(),'Notes')]"
    INTERACTIONS_TAB = "//span[contains(text(),'Interactions')]"
    ACTIVITY_LOGS_TAB = "//span[contains(text(),'Activity logs')]"
    ADD_ADDRESS_BUTTON = "//div[@id='Add Address']"
    MANAGE_CONTACT_DROPDOWN = "//div[@id='Manage Contact']"
    ADDRESS_FIELD = "//input[@id='line_1']"
    COUNTRY_SELECT = "country_code"
    SAVE_ADDRESS_BUTTON = "//span[normalize-space()='Save Address']"
    ADDRESSES_TABLE = "//h1[normalize-space()='Addresses']"
    UPLOAD_DOCUMENT_BUTTON = "//span[normalize-space()='Upload Document']"
    UPLOAD_DOCUMENT_INPUT = "//input[@id='file-contacts-document']"
    ADD_DOCUMENT_DESCRIPTION = "//textarea[@id='description']"
    AD_SAVE_DOCUMENT_BUTTON = "//span[normalize-space()='Save Document']"
    ADD_NOTES = "//span[normalize-space()='Add Note']"
    NOTES_FIELD = "//textarea[@id='note']"
    SAVE_NOTES_BUTTON = "//button[@type='submit']"
    ADD_EMPLOYMENT = "//span[normalize-space()='Add Employment']"
    AE_JOB_TITLE = "//input[@id='job_title']"
    ENTER_EMPLOYER_NAME_CHECKBOX = "//input[@id='organisation_type_new_organisation']"
    CHANGE_BUSINESS_UNIT = "//span[normalize-space()='Change Bus. Unit']"
    BUSINESS_UNIT_SELECT_FIELD = "//select[@id='business_unit']"
    CBU_CHANGE_BUTTON = "//button[@type='submit']"
    DEMOGRAPHICS = "//p[normalize-space()='Demographics']"
    BU_TEXT_FOR_ASSERTION = "//a[normalize-space()='World Health Organisation']"

    def get_details_tab(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.DETAILS_TAB)

    def get_employment_tab(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.EMPLOYMENT_TAB)

    def get_address_and_communication_tab(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.ADDRESS_AND_COMMUNICATION_TAB)

    def get_membership_tab(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.MEMBERSHIP_TAB)

    def get_subscription_tab(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.SUBSCRIPTION_TAB)

    def get_events_tab(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.EVENTS_TAB)

    def get_finance_tab(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.FINANCE_TAB)

    def get_document_tab(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.DOCUMENTS_TAB)

    def get_communication_tab(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.COMMUNICATION_TAB)

    def get_notes_tab(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.NOTES_TAB)

    def get_interaction_tab(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.INTERACTIONS_TAB)

    def get_activity_logs_tab(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.ACTIVITY_LOGS_TAB)

    def get_manage_contact_dropdown(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.MANAGE_CONTACT_DROPDOWN)

    def get_add_address_button(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.ADD_ADDRESS_BUTTON)

    def get_address_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.ADDRESS_FIELD)

    def get_country_select(self):
        return self.wait_for_visibility_of_element_located(By.ID, self.COUNTRY_SELECT)

    def get_save_address_button(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.SAVE_ADDRESS_BUTTON)

    def get_addresses_table(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.ADDRESSES_TABLE)

    def get_upload_document_button(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.UPLOAD_DOCUMENT_BUTTON)

    def get_upload_document_input(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.UPLOAD_DOCUMENT_INPUT)

    def get_add_document_description(self):
        return self.driver.find_element(By.XPATH, self.ADD_DOCUMENT_DESCRIPTION)

    def get_ad_save_document_button(self):
        return self.driver.find_element(By.XPATH, self.AD_SAVE_DOCUMENT_BUTTON)

    def get_add_notes(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.ADD_NOTES)

    def get_notes_field(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.NOTES_FIELD)

    def get_save_notes_button(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.SAVE_NOTES_BUTTON)

    def get_add_employment(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.ADD_EMPLOYMENT)

    def get_enter_employer_name_checkbox(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.ENTER_EMPLOYER_NAME_CHECKBOX)

    def get_ae_job_title(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.AE_JOB_TITLE)

    def get_change_business_unit(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CHANGE_BUSINESS_UNIT)

    def get_business_unit_select_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.BUSINESS_UNIT_SELECT_FIELD)

    def get_cbu_change_button(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CBU_CHANGE_BUTTON)

    def get_demographics_header(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.DEMOGRAPHICS)

    def get_bu_text_for_assertion(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.BU_TEXT_FOR_ASSERTION)

    def view_tab_details(self):
        self.get_address_and_communication_tab().click()
        time.sleep(4)
        self.get_membership_tab().click()
        time.sleep(4)
        self.get_subscription_tab().click()
        time.sleep(4)
        self.get_finance_tab().click()
        time.sleep(4)
        self.get_events_tab().click()
        time.sleep(4)
        self.get_notes_tab().click()



    def add_new_note(self, note):
        self.get_manage_contact_dropdown().click()
        time.sleep(2)
        self.get_add_notes().click()
        self.get_notes_field().send_keys(note)
        self.get_save_notes_button().click()

    # figure out how to select the date
    def get_add_employment(self,job_title, start_date, end_date):
        self.get_manage_contact_dropdown().click()
        time.sleep(2)
        self.get_add_employment().click()

        self.get_enter_employer_name_checkbox().click()
        self.get_ae_job_title().send_keys(job_title)
        start_date_element = self.wait_for_visibility_of_element_located(By.XPATH, f"//input[@value='{start_date}']")
        start_date_element.click()
        end_date_element = self.wait_for_visibility_of_element_located(By.XPATH, f"//input[@value='{end_date}']")
        end_date_element.click()

    def change_business_unit(self, business_unit):
        self.get_manage_contact_dropdown().click()
        self.get_change_business_unit().click()
        self.select_by_visible_text(business_unit, self.get_business_unit_select_field())
        time.sleep(2)
        self.get_cbu_change_button().click()
        time.sleep(2)
