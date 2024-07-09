import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage
from logic.home_page import HomePage


class LoginPage(BasePage):
    EMAIL_INPUT = '//input[@type="email"]'
    PASSWORD_INPUT = '//input[@type="password"]'
    SIGN_IN_BUTTON = '//input[@value="Sign in"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._email_input = self._driver.find_element(By.XPATH, self.EMAIL_INPUT)
        self._password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)

    def fill_username_input(self, username):
        WebDriverWait(self._driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, self.EMAIL_INPUT)))
        self._email_input.send_keys(username)

    def fill_password_input(self, password):
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.PASSWORD_INPUT)))
        self._password_input.send_keys(password)

    def click_on_sign_in_button(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.SIGN_IN_BUTTON)))
        element.click()

    # def login_flow(self, config):
    #     # Wait for the page to load
    #     home_page = HomePage(self._driver)
    #     home_page.click_on_login_button()
    #
    #     self.fill_username_input(config["email"])
    #     self.click_on_next_button()
    #
    #     self.fill_password_input(config["password"])
    #     time.sleep(1)
    #     self.click_on_next_button()
    #     time.sleep(7)
