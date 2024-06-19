import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
load_dotenv()





@pytest.fixture(scope="class")
def setup(request, browser):

    # # first driver instance to manage ceberus task
    # if browser == "chrome":
    #     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # elif browser == "firefox":
    #     driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    # elif browser == "edge":
    #     driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))


    username = os.getenv("EMAIL_USERNAME")
    ceberus_username = os.getenv("CEBERUS_EMAIL")
    password = os.getenv("PASSWORD")

    # wait = WebDriverWait(driver, 20)

    # # go to ceberus to reset tenant
    # driver.get("https://cerberus.memberbase-test.com/crm/")
    # driver.maximize_window()
    # driver.find_element(By.XPATH, "//input[@id='email']").send_keys(ceberus_username)
    # driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
    # driver.find_element(By.XPATH, "//span[@type='submit']").click()
    # driver.find_element(By.XPATH, "//a[normalize-space()='Tenants']").click()
    # time.sleep(2)
    # # search tenant
    # driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("world")
    # time.sleep(4)
    # # view tenant
    # driver.find_element(By.XPATH, "(//*[name()='svg'][@role='presentation'])[4]").click()
    # time.sleep(4)
    # driver.find_element(By.XPATH, "//div[@id='Management']").click()
    # wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Reset Tenant']"))).click()
    # wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']"))).click()
    # time.sleep(7)
    # driver.refresh()
    # time.sleep(8)
    # driver.quit()

    # # second driver instance to manage tenant task
    if browser == "chrome":
        driver1 = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver1 = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "edge":
        driver1 = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    # wait = WebDriverWait(driver1, 20)

# continue to the tenant
    # driver1.get("https://world-health-organisation.memberbase-test.com/crm")
    driver1.get("http://compsoc.memberbase.localhost/crm")
    driver1.maximize_window()
    driver1.find_element(By.XPATH, "//input[@id='email']").send_keys(username)
    driver1.find_element(By.XPATH, "//input[@id='password']").send_keys("PinkBlossom123!")
    time.sleep(2)
    driver1.find_element(By.XPATH, "//span[@type='submit']").click()

    request.cls.driver = driver1
    yield
    driver1.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope= "class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")
