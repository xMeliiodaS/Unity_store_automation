import logging
import unittest
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
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
        self.login_page.login_flow(self.config["email"], self.config["password"])
        logging.info("Logged into the unity asset store")
        self.home_page = HomePage(self.driver)

        self.home_page.click_on_account_button()
        self.home_page.click_on_personal_settings_button()

    def test_edit_bio_successful(self):
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
        print(current_text_in_bio)
        # Assert
        self.assertEqual(text_to_insert, current_text_in_bio)

    def test_edit_bio_with_invalid_data(self):
        """
        Test editing the bio with invalid data (e.g., exceeding character limit).
        """
        # Arrange
        personal_settings_page = PersonalSettingsPage(self.driver)
        personal_settings_page.click_on_edit_bio_button()

        # Act
        personal_settings_page.fill_bio_input("a" * 201)
        personal_settings_page.click_on_save_bio_button()

        # Assert
        current_text_in_bio = personal_settings_page.get_current_bio_text()
        self.assertLessEqual(len(current_text_in_bio), 200)


if __name__ == "__main__":
    unittest.main()
