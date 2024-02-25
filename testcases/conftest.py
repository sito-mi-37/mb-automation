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


@pytest.fixture(scope="class")
def setup(request, browser):

    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))


    driver.get("https://world-health-organisation.memberbase-test.com/crm")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//input[@id='email']").send_keys("admin@memberbasecrm.com")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("PinkBlossom123!")
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[@type='submit']").click()
    request.cls.driver = driver
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope= "class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")
