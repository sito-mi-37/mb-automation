from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class OrganisationListPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    VIEW_ORGANISATION = "//tbody/tr[1]/td[9]/div[1]/span[1]/a[1]//*[name()='svg']"
    EDIT_ORGANISATION = "//tbody/tr[1]/td[9]/div[1]/span[2]/a[1]//*[name()='svg']"

    def get_view_organisation_button(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.VIEW_ORGANISATION)

    def get_edit_organisation_button(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.VIEW_ORGANISATION)



