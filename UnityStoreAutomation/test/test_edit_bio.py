import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.cart_page import CartPage
from logic.home_page import HomePage
from logic.login_page import LoginPage
from logic.personal_settings_page import PersonalSettingsPage


class TestEditBio(unittest.TestCase):

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

        self.home_page.click_on_account_button()
        self.home_page.click_on_personal_settings_button()

    def tearDown(self) -> None:
        self.cart_page = CartPage(self.driver)
        self.cart_page.click_remove_asset_from_cart_button()
        self.driver.quit()

    def test_add_to_cart_successful(self):
        """
        Test the login functionality with valid credentials.
        """
        # Arrange
        personal_settings_page = PersonalSettingsPage(self.driver)
        personal_settings_page.click_on_edit_bio_button()

        # Act
        text_to_insert = self.config["bio_text"]
        personal_settings_page.fill_bio_input(text_to_insert)
        personal_settings_page.click_on_save_bio_button()
        current_text_in_bio = personal_settings_page.get_current_bio_text()

        # Assert
        self.assertEqual(text_to_insert, current_text_in_bio)


if __name__ == "__main__":
    unittest.main()
