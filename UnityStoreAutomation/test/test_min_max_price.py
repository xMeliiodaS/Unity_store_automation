import unittest
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.asset_page import AssetPage
from logic.cart_page import CartPage
from logic.home_page import HomePage
from logic.login_page import LoginPage


class TestMinMaxPrice(unittest.TestCase):

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
        self.home_page.click_on_pricing_button()
        self.home_page.fill_max_min_price_inputs_flow(self.config["max_price"],
                                                      self.config["min_price"])

        # Act
        sorted_prices = self.home_page.process_and_sort_asset_prices()

        # Assert
        self.assertGreaterEqual(sorted_prices[0], 500, "Minimum price is not greater"
                                                       " than or equal to $500")
        self.assertLessEqual(sorted_prices[-1], 1000, "Maximum price is not less"
                                                      " than or equal to $1000")


if __name__ == "__main__":
    unittest.main()
