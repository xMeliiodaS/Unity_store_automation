import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
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
        # Initialize the undetected ChromeDriver
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])
        self.home_page = HomePage(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_login_successful(self):
        """
        Test the login functionality with valid credentials.
        """
        # Arrange
        login_page = LoginPage(self.driver)

        # Act
        login_page.login_flow(self.config["email"], self.config["password"])
        login_page.click_on_sign_in_button()

        # Assert
        self.assertEqual(self.driver.current_url, "https://assetstore.unity.com/3d")

    def test_login_unsuccessful(self):
        """
        Test the login functionality with valid credentials.
        """
        # Arrange
        login_page = LoginPage(self.driver)

        # Act
        login_page.login_flow(self.config["email"], self.config["incorrectpassword"])
        login_page.click_on_sign_in_button()

        # Assert
        self.assertNotEqual(self.driver.current_url, "https://assetstore.unity.com/3d")


if __name__ == "__main__":
    unittest.main()
