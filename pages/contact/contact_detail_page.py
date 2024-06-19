import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from datetime import date

from base.base_driver import BaseDriver


class ContactDetailPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # -------------------------------------- CONSTANTS --------------------------------------------------

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
   
#    -----------MEMBERSHIP CONSTANTS----------------
    MEMBERSHIP_DROPDOWN = "//div[@id='Membership']"
    ACTIVATE_MEMBERSHIP_BUTTON = "//span[normalize-space()='Activate Membership']"
    SOLE_MEMBERSHIP_CHECKBOX = "membership_link_1"
    SOLE_MEMBERSHIP_TYPE_SELECT_FIELD = "//select[@id='membership_type_id']"
    SOLE_PAYMENT_METHOD_SELECT_FIELD = "//select[@id='payment_method']"
    SOLE_MEMBERSHIP_ACTIVATE_BUTTON = "//button[@type='submit']"
    
    CHANGE_MEMBERSHIP_TYPE = "//span[normalize-space()='Change Membership Type']"
    CM_NEW_MEMBERSHIP_TYPE_SELECT_FIELD = "//select[@id='membership_type']"
    CM_WHEN_IMMEDIATELY_CHECK_BOX = "//input[@id='when_immediately']"
    CM_INVOICE_THE_CUSTOMER_CHECKBOX ="//input[@id='invoice_or_credit_action_invoice']"
    CM_AMOUNT = "//input[@id='amount']"
    CM_CHANGE_BUTTON = "//span[normalize-space()='Change']"
    CM_NONE_CHECKBOX_FIELD = "//input[@id='invoice_or_credit_action_no_action']"
    CM_CREDIT_THE_CUSTOMER = "//input[@id='invoice_or_credit_action_credit']"

    CANCEL_MEMBERSHIP = "//span[normalize-space()='Cancel Membership']"
    CANCEL_MEMBERSHIP_ACTION_SUSPEND = "action_1"
    CANCEL_MEMBERSHIP_ACTION_DO_NOT_RENEW = "action_2"
    CANCEL_MEMBERSHIP_DATE_LEFT = f"//input[@placeholder='{date.today()}']"
    CANCEL_MEMBERSHIP_REASON_FOR_LEAVING = "//select[@id='leave_reason_id']"
    CANCEL_MEMBERSHIP_SUBMIT_BUTTON = "//button[@type='submit']"

    INVOICED_TO_ELEMENT = "//h4[normalize-space()='Invoiced To']"
    MEMBERSHIP_TAB_ADJUST_DATE_BUTTON = "//button[normalize-space()='Adjust Dates']"

    CHANGE_MEMBERSHIP_NUMBER_BUTTON = "//span[normalize-space()='Change Membership Number']"
    NEW_MEMBERSHIP_NUMBER_INPUT_FIELD = "//input[@id='new_membership_number']"
    CHANGE_NUMBER_SUBMIT_BUTTON = "//span[normalize-space()='Change Number']"

    FINANCE_DROPDOWN = "//div[@id='Finance']"
    CREATE_INVOICE = "//span[normalize-space()='Create Invoice']"
    CI_PRODUCT_CATEGORY_SELECT_FIELD = "//select[@id='product']"
    CI_PRODUCT_SELECT_FIELD = "//select[@id='productItem']"
    CI_DUE_DATE = "//input[@class='w-full form-control form-input form-input-bordered input active']"
    CI_VAT = "//select[@id='VAT']"
    CI_LINE_1 = "(//input[@id='invoice_address_line_1'])[1]"
    CI_CITY = "//input[@id='invoice_address_city']"
    CI_STATE = "//input[@id='invoice_address_state']"
    CI_COUNTRY = "//select[@id='invoice_address_country']"
    CI_CREATE_INVOICE_BUTTON = "//button[@type='submit']"

    VIEW_FIRST_INVOICE_ITEM = "(//*[name()='svg'][@role='presentation'])[5]"
    SETTLE_INVOICE_DROPDOWN = "//div[@id='Settle Invoice']"
    CREDIT_INVOICE_OPTION = "//span[normalize-space()='Credit Invoice']"
    CRIN_AMOUNT_TO_CREDIT = "//input[@id='amount_credited']"
    CRIN_NOTE = "//textarea[@id='note']"
    CRIN_YES_APPLY_CREDIT_BUTTON = "//button[@type='submit']"

    POST_INVOICE_OPTION = "//span[normalize-space()='Capture Payment']"
    POIN_AMOUNT_PAID = "//input[@id='amount_paid']"
    POIN_DATE_RECIEVED = f"//input[@placeholder='{date.today()}']"
    POIN_PAYMENT_PROVIDER_SELECT_FIELD = "//select[@id='payment_provider']"
    POIN_DESCRIPTION_TEXTAREA = "//textarea[@id='description']"
    POIN_POST_PAYMENT_SUBMIT_BUTTON = "//button[@type='submit']"

    




    # -------------------------------------- ELEMENTS --------------------------------------------------

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
    
    # ------------------MEMBERSHIP ELEMNTS---------------
    def get_membership_dropdown(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.MEMBERSHIP_DROPDOWN)
    
    def get_activate_membership_button(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.ACTIVATE_MEMBERSHIP_BUTTON)
    
    def get_sole_membership_checkbox(self):
        return self.wait_for_visibility_of_element_located(By.ID, self.SOLE_MEMBERSHIP_CHECKBOX)

    def get_sole_membership_type_select_field(self):
        return self.wait_for_visibility_of_element_located(By.ID, self.SOLE_MEMBERSHIP_TYPE_SELECT_FIELD)
    
    def get_sole_membership_payment_method(self):
        return self.wait_for_visibility_of_element_located(By.ID, self.SOLE_PAYMENT_METHOD_SELECT_FIELD)
    
    def get_sole_membership_activate_button(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.SOLE_MEMBERSHIP_ACTIVATE_BUTTON)
    


    def get_change_membership_type(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CHANGE_MEMBERSHIP_TYPE)
 
    def get_new_membership_type_select_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CM_NEW_MEMBERSHIP_TYPE_SELECT_FIELD)
    
    def get_when_immediately_checkbox(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CM_IMMEDIATELY_CHECK_BOX)
    
    def get_cm_invoice_the_customer_checkbox(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CM_INVOICE_THE_CUSTOMER_CHECKBOX)
    
    def get_cm_amount(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CM_AMOUNT)
    

    def get_cm_change_button(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CM_CHANGE_BUTTON)
    
    def get_cm_none_checkbox_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CM_NONE_CHECKBOX_FIELD)
    
    def get_cm_credit_the_customer(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CM_CREDIT_THE_CUSTOMER)
    
    def get_invoiced_to(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.INVOICED_TO_ELEMENT)
    
    def get_membership_tab_adjust_date_button(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.MEMBERSHIP_TAB_ADJUST_DATE_BUTTON)
    
    def get_change_membership_number_button(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CHANGE_MEMBERSHIP_NUMBER_BUTTON)
    
    def get_new_membership_number_input_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.NEW_MEMBERSHIP_NUMBER_INPUT_FIELD)
    
    def get_change_number_submit_button(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CHANGE_NUMBER_SUBMIT_BUTTON)
    
    def get_finance_dropdown(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.FINANCE_DROPDOWN)
    
    def get_create_invoice(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CREATE_INVOICE)
    
    def get_ci_product_category_select_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CI_PRODUCT_CATEGORY_SELECT_FIELD)
    
    def get_ci_product_select_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CI_PRODUCT_SELECT_FIELD)

    def get_ci_due_date(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CI_DUE_DATE)
    
    def get_ci_vat(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CI_VAT)
    
    def get_ci_line1(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CI_LINE_1)
    
    def get_ci_city(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CI_CITY)

    def get_ci_state(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CI_STATE)
    
    def get_ci_country(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CI_COUNTRY)

    def get_ci_create_invoice_button(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CI_CREATE_INVOICE_BUTTON)
    

    def get_view_first_invoice_item(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.VIEW_FIRST_INVOICE_ITEM)
    
    def get_settle_invoice_dropdown(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.SETTLE_INVOICE_DROPDOWN)
    
    def get_credit_invoice_option(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CREDIT_INVOICE_OPTION)
    
    def get_crin_amount_to_credit(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CRIN_AMOUNT_TO_CREDIT)
    
    def get_crin_note(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CRIN_NOTE)
    
    def get_crin_yes_apply_credit_button(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CRIN_YES_APPLY_CREDIT_BUTTON)
    
    def get_post_invoice_option(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.POST_INVOICE_OPTION)
    
    def get_poin_amount_paid(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.POIN_AMOUNT_PAID)
    
    def get_poin_date_recieved(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.POIN_DATE_RECIEVED)
    
    def get_poin_payment_provider_select_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.POIN_PAYMENT_PROVIDER_SELECT_FIELD)
    
    def get_poin_description_textarea(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.POIN_DESCRIPTION_TEXTAREA)
     
    def get_poin_post_payment_submit_button(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.POIN_POST_PAYMENT_SUBMIT_BUTTON)
    
    def get_cancel_membership(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CANCEL_MEMBERSHIP)

    def get_cancel_action_suspend_checkbox(self):
        return self.wait_for_element_to_be_clickable(By.ID, self.CANCEL_MEMBERSHIP_ACTION_SUSPEND)

    def get_cancel_membership_action_do_not_renew_checkbox(self):
        return self.wait_for_element_to_be_clickable(By.ID, self.CANCEL_MEMBERSHIP_ACTION_DO_NOT_RENEW)
    
    def get_cancel_membership_date_left(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CANCEL_MEMBERSHIP_DATE_LEFT)
    
    def get_cancel_membership_reason_for_leaving_select_field(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CANCEL_MEMBERSHIP_REASON_FOR_LEAVING)

    def get_cancel_membership_submit_button(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CANCEL_MEMBERSHIP_SUBMIT_BUTTON)



    # ------------------------------------- TEST METHODS -------------------------------------------

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

    def activate_sole_membership(self, membership_type, payment_method):
        self.get_membership_dropdown().click()
        self.get_activate_membership_button().click()
        self.get_sole_membership_checkbox().click()
        self.select_by_visible_text(membership_type, self.get_sole_membership_type_select_field()) 
        self.select_by_visible_text(payment_method, self.get_sole_membership_payment_method())
        time.sleep(2)
        self.get_sole_membership_activate_button().click()

    def cancel_contact_membership(self, action, date_left, reason_for_leaving):
        self.get_membership_dropdown().click()
        self.get_cancel_membership().click()
        if(action == "Suspend"):
            self.get_cancel_action_suspend_checkbox().click()
        else:
            self.get_cancel_action_suspend_checkbox().click()
        # add date selection
        self.select_by_visible_text(reason_for_leaving, self.get_cancel_membership_reason_for_leaving_select_field())


    def change_membership_type_pay(self, new_membership_type, amount):
        self.get_change_membership_type().click()
        self.select_by_visible_text(new_membership_type, self.get_new_membership_type_select_field())
        time.sleep(2)
        self.get_when_immediately_checkbox().click()
        self.get_cm_invoice_the_customer_checkbox().click()
        self.get_cm_amount().send_keys(amount)
        time.sleep(2)
        self.get_cm_change_button().click()
        time.sleep(4)

    def change_membership_type_no_pay(self, new_membership_type):
        self.get_change_membership_type().click()
        self.select_by_visible_text(new_membership_type, self.get_new_membership_type_select_field())
        self.get_when_immediately_checkbox().click()
        self.get_cm_none_checkbox_field().click()
        time.sleep(2)
        self.get_cm_change_button().click()


    def change_membership_type_credit_customer(self, new_membership_type, amount):
        self.get_change_membership_type().click()
        self.select_by_visible_text(new_membership_type, self.get_new_membership_type_select_field())
        time.sleep(2)
        self.get_when_immediately_checkbox().click()
        self.get_cm_credit_the_customer().click()
        self.get_cm_amount().send_keys(amount)
        time.sleep(2)
        self.get_cm_change_button().click()
        time.sleep(4)

    def change_membership_date(self, startDate, ):
        self.get_membership_tab().click()
        self.scroll_to_element(self.get_invoiced_to())
        self.get_membership_tab_adjust_date_button().click()
        # put the start date and end date

    def change_membership_number(self, new_membership_number):
        self.get_membership_dropdown().click()
        self.get_change_membership_number_button().click()
        self.get_new_membership_number_input_field().send_keys(new_membership_number)
        time.sleep(2)
        self.get_change_number_submit_button().click()
        time.sleep(5)

    def create_invoice(self, product_category, product, due_date,  vat, line1, city, state,country):
        self.get_finance_dropdown().click()
        self.get_create_invoice().click()
        time.sleep(2)
        self.select_by_visible_text(product_category, self.get_ci_product_category_select_field())
        self.select_by_visible_text(product, self.get_ci_product_select_field())
        # add date
        self.get_ci_due_date().click()
        # please add date to continue

        self.select_by_visible_text(vat, self.get_ci_vat())
        self.get_ci_line1().send_keys(line1)
        self.get_ci_city().send_keys(city)
        self.get_ci_state().send_keys(state)
        self.select_by_visible_text(country, self.get_ci_country())
        self.get_ci_create_invoice_button().click()

    def credit_customer_invoice(self, amount, notes):
        self.get_finance_tab().click()
        self.get_view_first_invoice_item().click()
        time.sleep(3)
        self.get_settle_invoice_dropdown().click()
        self.get_credit_invoice_option().click()
        self.get_crin_amount_to_credit().send_keys(amount)
        self.get_crin_note().send_keys(notes)
        self.get_crin_yes_apply_credit_button().click()
        time.sleep(3)

    def post_customer_invoice(self, amount, payment_method,description ):
        self.get_finance_tab().click()
        self.get_view_first_invoice_item().click()
        time.sleep(3)
        self.get_settle_invoice_dropdown().click()
        self.get_post_invoice_option().click()
        self.get_poin_amount_paid().send_keys(amount)
        # handle date recieved
        self.select_by_visible_text(payment_method, self.get_poin_payment_provider_select_field())
        self.get_poin_description_textarea().send_keys(description)
        self.get_poin_post_payment_submit_button().click()

   
