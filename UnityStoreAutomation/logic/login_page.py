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
    ERROR_MESSAGE = '//div[@class="error-msg"]'

    def __init__(self, driver):
        """
        Initialize the LoginPage with a WebDriver instance.

        :param driver: The WebDriver instance to use for browser interactions.
        """
        super().__init__(driver)

    def fill_username_input(self, username):
        """
        Fill in the username input field with the provided username.

        :param username: The username to enter into the email input field.
        """
        element = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.EMAIL_INPUT)))
        element.send_keys(username)

    def fill_password_input(self, password):
        """
        Fill in the password input field with the provided password.

        :param password: The password to enter into the password input field.
        """
        WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.PASSWORD_INPUT))).send_keys(password)

    def click_on_sign_in_button(self):
        """
        Click on the sign-in button.

        This method waits for the sign-in button to be present and then clicks on it.
        """
        element = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.SIGN_IN_BUTTON)))
        element.click()

    def login_flow(self, username, password):
        """
        Perform the login flow using the provided username and password.

        This method navigates to the login page, fills in the username and password fields,
        and submits the login form.

        :param username: The username to be used for login.
        :param password: The password to be used for login.
        """
        home_page = HomePage(self._driver)
        home_page.click_on_close_cookies_button()
        home_page.click_on_account_button()
        home_page.click_on_sign_in_button()

        self.fill_username_input(username)
        self.fill_password_input(password)
        self.click_on_sign_in_button()

    def is_login_error_message_displayed(self):
        time.sleep(1)
        return WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.ERROR_MESSAGE))).is_displayed()
