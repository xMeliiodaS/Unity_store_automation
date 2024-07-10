import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.asset_page import AssetPage
from logic.home_page import HomePage
from logic.login_page import LoginPage


class TestCartPage(unittest.TestCase):

    # Before all - Called automatically
    def setUp(self):
        """
        Set up the test environment before each test.

        This method initializes the browser, loads the configuration,
        and navigates to the specified URL.
        """
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])

        self.login_page = LoginPage(self.driver)
        self.login_page.login_flow(self.config)

    def tearDown(self) -> None:
        self.home_page = HomePage(self.driver)
        self.home_page.click_on_cart_button()
        self.home_page.click_remove_asset_from_cart_button()
        time.sleep(5)

    def test_add_to_cart_successful(self):
        """
        Test the login functionality with valid credentials.
        """
        # Arrange
        self.home_page = HomePage(self.driver)
        self.home_page.click_on_asset_link()
        asset_page = AssetPage(self.driver)

        # Act
        asset_page.click_on_add_to_cart_button()
        asset_page.click_on_cart_button()
        time.sleep(10)
        # Assert


if __name__ == "__main__":
    unittest.main()
