import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_forgot_password(setup):
    driver = setup
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    login_page = LoginPage(driver)
    
    login_page.click_forgot_password()
    login_page.enter_username("Admin")
    login_page.click_reset_password()
    
    # Add assertions here as needed
