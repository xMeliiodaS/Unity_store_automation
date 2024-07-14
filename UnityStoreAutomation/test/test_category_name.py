import logging
import unittest
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.logging_setup import logger_setup
from logic.asset_page import AssetPage
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
        logging.info("STARTING test for category name")

        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])

        self.login_page = LoginPage(self.driver)
        self.login_page.login_flow(self.config["email"], self.config["password"])
        logging.info(f"Logging in with email: {self.config['email']}")

        self.home_page = HomePage(self.driver)

    def tearDown(self) -> None:
        """
        Clean up after each test case by quitting the WebDriver instance.
        """
        self.driver.quit()

    def test_category_name_exist(self):
        """
        Test if a category name exists in the asset's path categories list.
        """
        # Arrange
        category_name = self.home_page.get_random_category_text()
        self.home_page.click_on_category_by_name(category_name)

        self.home_page.click_on_asset_link_by_index(2)

        # Act
        asset_page = AssetPage(self.driver)
        categories_list = asset_page.get_asset_path_categories_list_names()

        # Assert
        self.assertIn(category_name, categories_list)


if __name__ == "__main__":
    unittest.main()
