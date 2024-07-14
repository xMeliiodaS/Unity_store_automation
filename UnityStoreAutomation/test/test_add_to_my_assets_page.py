import logging
import unittest
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.logging_setup import logger_setup
from logic.asset_page import AssetPage
from logic.home_page import HomePage
from logic.login_page import LoginPage
from logic.my_assets_page import MyAssetsPage


class TestAddToMyAssetsPage(unittest.TestCase):

    # Before all - Called automatically
    def setUp(self):
        """
        Set up the test environment before each test.

        This method initializes the browser, loads the configuration,
        and navigates to the specified URL.
        """
        logging.info("----------STARTING TESTING Add asset to My Assets----------")

        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])

        self.login_page = LoginPage(self.driver)
        self.login_page.login_flow(self.config["email"], self.config["password"])
        logging.info(f"Logging in with email: {self.config['email']}")

        self.home_page = HomePage(self.driver)
        self.home_page.free_asset_navigation_flow(20)

        self.asset_page = AssetPage(self.driver)
        self.asset_name = self.asset_page.get_asset_title()

    def test_add_asset_to_my_assets_successful(self):
        """
        Test adding an asset to 'My Assets' successfully.
        """
        # Arrange
        self.asset_page.add_and_view_my_assets_flow()

        # Act
        my_assets_page = MyAssetsPage(self.driver)
        assets_name_list = my_assets_page.get_assets_name()

        # Assert
        self.assertIn(self.asset_name, assets_name_list)
        logging.info("---------------TEST COMPLETED---------------")

    def tearDown(self):
        """
        Clean up after each test case by quitting the WebDriver instance.
        """
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
