import logging
import unittest
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.logging_setup import logger_setup
from logic.enum.asset_per_page_options import AssetsPerPageOptions
from logic.home_page import HomePage
from logic.login_page import LoginPage


class TestDropdownViewResults(unittest.TestCase):

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

        self.login_page = LoginPage(self.driver)
        self.login_page.login_flow(self.config["email"], self.config["password"])
        self.home_page = HomePage(self.driver)

    def test_assets_count_changed_after_dropdown(self):
        """
        Test if the assets count changes after selecting a different option from the dropdown.
        """
        logging.info("----------TESTING assets count change after dropdown selection STARTED----------")
        logging.info(f"Logged in with email: {self.config['email']}")

        # Arrange
        assets_count_before = self.home_page.get_current_assets_count_in_page()
        self.home_page.click_on_view_results_dropdown_button()

        # Act
        self.home_page.select_from_dropdown_by_value(AssetsPerPageOptions.SEVENTY_TWO.value)

        # Assert
        self.assertNotEqual(assets_count_before, self.home_page.get_current_assets_count_in_page())
        logging.info("--------------------------TEST COMPLETED---------------------------\n\n")

    def test_assets_count_match_chosen_option(self):
        """
        Test if the assets count matches the chosen option from the dropdown.
        """
        logging.info("----------TESTING assets count match chosen option from dropdown STARTED----------")
        logging.info(f"Logged in with email: {self.config['email']}")

        # Arrange
        self.home_page.click_on_view_results_dropdown_button()

        # Act
        option_value = AssetsPerPageOptions.SEVENTY_TWO.value
        self.home_page.select_from_dropdown_by_value(option_value)

        # Assert
        self.assertEqual(option_value, self.home_page.get_current_assets_count_in_page())
        logging.info("--------------------------TEST COMPLETED---------------------------\n\n")

    def tearDown(self):
        """
        Clean up after each test case by quitting the WebDriver instance.
        """
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
