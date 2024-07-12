import time
import unittest
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
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
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])

        self.login_page = LoginPage(self.driver)
        self.login_page.login_flow(self.config["email"], self.config["password"])
        self.home_page = HomePage(self.driver)

    def test_min_max_price_valid(self):
        """
        Test the login functionality with valid credentials.
        """
        # Arrange
        self.home_page.click_on_view_results_dropdown_button()
        self.home_page.select_from_dropdown()
        time.sleep()

        # Act

        # Assert


if __name__ == "__main__":
    unittest.main()
