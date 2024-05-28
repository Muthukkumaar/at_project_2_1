import logging
from selenium.common.exceptions import NoSuchElementException

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.forgot_password_link = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p')
        self.username_field = (By.NAME, 'username')
        self.reset_password_button = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]')

    def click_forgot_password(self):
        try:
            self.driver.find_element(*self.forgot_password_link).click()
        except NoSuchElementException as e:
            logging.error(f"Element not found: {e}")

    def enter_username(self, username: str):
        try:
            self.driver.find_element(*self.username_field).send_keys(username)
        except NoSuchElementException as e:
            logging.error(f"Element not found: {e}")

    def click_reset_password(self):
        try:
            self.driver.find_element(*self.reset_password_button).click()
        except NoSuchElementException as e:
            logging.error(f"Element not found: {e}")
