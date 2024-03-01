import time
import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def set_up(request):

    print("Start Test")
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities["pageLoadStrategy"] = "eager"
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": f"{os.getcwd()}/file_folder"}
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)
    request.cls.driver = driver
    yield
    print("Finish Test")

    time.sleep(10)
    driver.quit()


@pytest.fixture(scope="module")
def set_group():
    print("Enter System")
    yield
    print("Exit System")
