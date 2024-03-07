import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BaseDriver():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    MEMBERBASE_LOGO = "(//img)[1]"
    def wait_for_element_to_be_clickable(self, locator_type, locator):
        element = self.wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element

    def wait_for_visibility_of_element_located(self, locator_type, locator):
        element = self.wait.until(EC.visibility_of_element_located((locator_type, locator)))
        return element

    def return_to_dashboard(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.MEMBERBASE_LOGO).click()

    def scroll_by_pixel(self, pixel):
        self.driver.execute_script(f"window.scrollBy(0,{pixel})", "")

    def scroll_to_page_bottom(self):
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_to_page_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)


    def select_by_visible_text(self, value, element):
        cs = Select(element)
        cs.select_by_visible_text(value)
        time.sleep(2)