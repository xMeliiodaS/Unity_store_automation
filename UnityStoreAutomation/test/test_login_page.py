import logging
import unittest
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.logging_setup import logger_setup
from logic.home_page import HomePage
from logic.login_page import LoginPage


class TestLoginPage(unittest.TestCase):

    # Before all - Called automatically
    def setUp(self):
        """
        Set up the test environment before each test.

        This method initializes the browser, loads the configuration,
        and navigates to the specified URL.
        """
        logging.info("------------------------------SETUP------------------------------")

        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])
        self.home_page = HomePage(self.driver)

    def tearDown(self) -> None:
        """
        Clean up after each test case by quitting the WebDriver instance.
        """
        self.driver.quit()

    def test_login_successful(self):
        """
        Test the login functionality with valid credentials.
        """
        logging.info("----------TESTING login with valid credentials STARTED----------")

        # Arrange
        login_page = LoginPage(self.driver)

        # Act
        login_page.login_flow(self.config["email"], self.config["password"])
        self.home_page.click_on_account_button()

        # Assert
        self.assertTrue(self.home_page.is_logout_displayed())
        logging.info("--------------------------TEST COMPLETED---------------------------\n\n")

    def test_login_unsuccessful(self):
        """
        Test the login functionality with invalid credentials.
        """
        logging.info("----------TESTING login with invalid credentials STARTED----------")

        # Arrange
        login_page = LoginPage(self.driver)

        # Act
        login_page.login_flow(self.config["email"], self.config["incorrect_password"])

        # Assert
        self.assertTrue(login_page.is_login_error_message_displayed())
        logging.info("--------------------------TEST COMPLETED---------------------------\n\n")


if __name__ == "__main__":
    unittest.main()
