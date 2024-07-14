import logging
import unittest
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.asset_page import AssetPage
from logic.cart_page import CartPage
from logic.home_page import HomePage
from logic.login_page import LoginPage
from infra.logging_setup import logger_setup


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
        self.login_page.login_flow(self.config["email"], self.config["password"])
        logging.info(f"Logging in with email: {self.config['email']}")

        self.home_page = HomePage(self.driver)

    def tearDown(self) -> None:
        """
        Clean up after each test case by removing the asset from
         the cart and quitting the WebDriver instance.
        """
        self.cart_page = CartPage(self.driver)
        self.cart_page.click_remove_asset_from_cart_button()
        self.driver.quit()

    def test_add_to_cart_successful(self):
        """
        Test adding an asset to the cart and verifying its presence.
        """
        # Arrange
        self.home_page.click_on_asset_link()
        asset_page = AssetPage(self.driver)
        asset_title = asset_page.get_asset_title()

        # Act
        asset_page.add_asset_to_cart_flow()
        cart_page = CartPage(self.driver)
        asset_in_cart_title = cart_page.get_asset_in_cart_title()

        # Assert
        self.assertEqual(asset_title, asset_in_cart_title)


if __name__ == "__main__":
    unittest.main()
