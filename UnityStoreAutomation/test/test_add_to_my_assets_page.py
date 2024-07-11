import time
import unittest
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
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
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])

        self.login_page = LoginPage(self.driver)
        self.login_page.login_flow(self.config)
        self.home_page = HomePage(self.driver)

    def test_category_name_exist(self):
        """
        Test the login functionality with valid credentials.
        """
        # Arrange
        self.home_page.click_on_pricing_button()
        self.home_page.click_on_free_assets_button()
        self.home_page.click_on_asset_link_by_index(1)

        asset_page = AssetPage(self.driver)
        asset_name = asset_page.get_asset_title()

        asset_page.click_on_add_to_my_assets_button()
        asset_page.click_on_accept_to_my_assets_button()
        asset_page.click_on_my_assets_button()
        my_assets_page = MyAssetsPage(self.driver)

        # Act
        assets_name_list = my_assets_page.get_assets_name()

        # Assert
        self.assertIn(asset_name, assets_name_list)


if __name__ == "__main__":
    unittest.main()
