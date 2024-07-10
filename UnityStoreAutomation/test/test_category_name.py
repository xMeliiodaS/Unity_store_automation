import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.asset_page import AssetPage
from logic.cart_page import CartPage
from logic.home_page import HomePage
from logic.login_page import LoginPage


class TestCategory(unittest.TestCase):

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

    def test_category_name_exist(self):
        """
        Test the login functionality with valid credentials.
        """
        # Arrange
        home_page = HomePage(self.driver)
        category_name = home_page.get_random_category_text()
        home_page.click_on_category_by_name(category_name)

        home_page.click_on_asset_link()

        # Act
        asset_page = AssetPage(self.driver)
        categories_list = asset_page.get_asset_path_categories_list_names()
        # Assert
        self.assertIn(category_name, categories_list)


if __name__ == "__main__":
    unittest.main()
