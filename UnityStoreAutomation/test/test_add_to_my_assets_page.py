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
        self.home_page.free_asset_navigation_flow(1)

        self.asset_page = AssetPage(self.driver)
        self.asset_name = self.asset_page.get_asset_title()

    def test_category_name_exist(self):
        """
        Test the login functionality with valid credentials.
        """
        # Arrange
        self.asset_page.add_asset_to_cart_flow()

        # Act
        my_assets_page = MyAssetsPage(self.driver)
        assets_name_list = my_assets_page.get_assets_name()

        # Assert
        self.assertIn(self.asset_name, assets_name_list)


if __name__ == "__main__":
    unittest.main()
