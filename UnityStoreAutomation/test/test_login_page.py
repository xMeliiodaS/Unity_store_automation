import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.home_page import HomePage
from logic.login_page import LoginPage


class TestLoginPage(unittest.TestCase):

    # Before all - Called automatically
    def setUp(self):
        # Initialize the undetected ChromeDriver
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])
        self.home_page = HomePage(self.driver)

    def test_login_successful(self):
        # Arrange
        self.home_page.click_on_account_button()
        time.sleep(2)
        self.home_page.click_on_sign_in_button()

        # Act
        login_page = LoginPage(self.driver)
        login_page.fill_username_input(self.config["email"])
        login_page.fill_password_input(self.config["password"])
        login_page.click_on_sign_in_button()
        time.sleep(5)

        # Assert
        self.assertEqual(self.driver.current_url, "https://assetstore.unity.com/")
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
