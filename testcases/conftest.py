import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def setup(request):
    # Launch browser and login
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get("https://agcas.memberbase-test.com/crm")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//input[@id='email']").send_keys("admin@memberbasecrm.com")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("PinkBlossom123!")
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[@type='submit']").click()
    request.cls.driver = driver
    yield
    driver.close()
