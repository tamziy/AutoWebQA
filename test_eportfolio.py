import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    
    yield driver
    
    driver.quit
    
def test_title(driver):
    driver.get("https://www.tamziy.com")
    assert "tamziy" in driver.title