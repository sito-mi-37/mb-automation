import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class GroupListPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    CREAT_GROUP_CATRGORIES_BUTTON = "//div[contains(text(),'Create Group Category')]"
    CGC_DISPLAY_NAME_INPUT_FIELD = "//input[@id='Display Name']"
    CGC_NAME_INPUT_FIELD = "//input[@id='Name']"
    CGC_DESCRIPTION_INPUT_FIELD = "//textarea[@id='description']"
    CGC_SAVE_CATEGORY_BUTTON = "//span[normalize-space()='Save category']"
    CGC_CREATE_GROUP_BUTTON = "(//div[@class='text-sm py-2 font-light'])[1]"
    CGC_CG_NAME_INPUT_FIELD = "//input[@id='name']"
    CGC_CG_DESCRIPTION_INPUT_FIELD = "//textarea[@id='description']"
    CGC_CG_TYPE_SELECT_FIELD = "//select[@id='type']"
    CGC_CG_SAVE_GROUP_BUTTON = "//span[normalize-space()='Save group']"
    CREATE_GROUP = "(//div[@class='text-sm py-2 font-light'][normalize-space()='Create Group'])[1]"
    EDIT_FIRST_GROUP_BUTTON = "(//*[name()='svg'][@role='presentation'])[5]"
    UPDATE_GROUP_BUTTON = "//span[normalize-space()='Update Group']"
    
    def get_group_categories_button(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CREAT_GROUP_CATRGORIES_BUTTON)
    
    def get_cgc_display_name_input_field(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CGC_DISPLAY_NAME_INPUT_FIELD)
    
    def get_cgc_name_input_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CGC_NAME_INPUT_FIELD)
    
    def get_cgc_description_input_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CGC_DESCRIPTION_INPUT_FIELD)
    
    def get_cgc_save_category_button(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CGC_SAVE_CATEGORY_BUTTON)
    
    def get_cgc_create_group_button(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CGC_CREATE_GROUP_BUTTON)
    
    def get_cgc_cg_name_input_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CGC_CG_NAME_INPUT_FIELD)
    
    def get_cgc_cg_description_input_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CGC_CG_DESCRIPTION_INPUT_FIELD)
    
    def get_cgc_cg_type_select_field(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.CGC_CG_TYPE_SELECT_FIELD)
    
    def get_cgc_cg_save_group_button(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CGC_CG_SAVE_GROUP_BUTTON)
    
    def get_create_group_button(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CREATE_GROUP)
    
    def get_edit_first_group_button(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.EDIT_FIRST_GROUP_BUTTON)
    
    def get_update_group_button(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.UPDATE_GROUP_BUTTON)
    
    def create_group_category(self, category_display_name, category_name, category_desc ):
        self.get_group_categories_button().click()
        time.sleep(4)
        self.get_cgc_display_name_input_field().send_keys(category_display_name)
        time.sleep(1)
        self.get_cgc_name_input_field().send_keys(category_name)
        time.sleep(1)
        self.get_cgc_description_input_field().send_keys(category_desc)
        time.sleep(1)
        self.get_cgc_save_category_button().click()
        time.sleep(3)

    def create_group(self, group_name, group_description, group_type):
        self.get_create_group_button().click()  
        time.sleep(3)
        self.get_cgc_cg_name_input_field().send_keys(group_name)
        time.sleep(1)
        self.get_cgc_cg_description_input_field().send_keys(group_description)
        time.sleep(1)   
        self.select_by_visible_text(group_type, self.get_cgc_cg_type_select_field())
        time.sleep(1)
        self.get_cgc_cg_save_group_button().click()
        time.sleep(3)

    def update_group(self, group_name, group_description):
        self.get_edit_first_group_button().click()
        time.sleep(3)
        self.get_cgc_cg_name_input_field().clear()
        time.sleep(1)
        self.get_cgc_cg_name_input_field().send_keys(group_name)
        self.get_cgc_cg_description_input_field().clear()
        time.sleep(1)
        self.get_cgc_cg_description_input_field().send_keys(group_description)
        time.sleep(1)
        self.get_update_group_button().click()
        time.sleep(3)
        
