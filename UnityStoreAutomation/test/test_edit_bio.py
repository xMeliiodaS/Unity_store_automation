import logging
import unittest
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.logging_setup import logger_setup
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
        logging.info("STARTING test for the editing BIO")

        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])

        self.login_page = LoginPage(self.driver)
        self.login_page.login_flow(self.config["email"], self.config["password"])
        logging.info(f"Logging in with email: {self.config['email']}")

        self.home_page = HomePage(self.driver)
        self.home_page.click_on_account_button()
        self.home_page.click_on_personal_settings_button()

        self.personal_settings_page = PersonalSettingsPage(self.driver)
        self.personal_settings_page.click_on_edit_bio_button()

    def test_edit_bio_successful(self):
        """
        Test the login functionality with valid credentials.
        """
        # Act
        text_to_insert = self.config["bio_text"]
        self.personal_settings_page.fill_bio_input(text_to_insert)
        self.personal_settings_page.click_on_save_bio_button()
        current_text_in_bio = self.personal_settings_page.get_current_bio_text()

        # Assert
        self.assertEqual(text_to_insert, current_text_in_bio)

    def test_edit_bio_with_invalid_data(self):
        """
        Test editing the bio with invalid data (e.g., exceeding character limit).
        """
        # Act
        self.personal_settings_page.fill_bio_input(self.config["bio_text_exceeding_limit"] * 201)
        self.personal_settings_page.click_on_save_bio_button()

        # Assert
        current_text_in_bio = self.personal_settings_page.get_current_bio_text()
        self.assertLessEqual(len(current_text_in_bio), 200)

    def tearDown(self):
        """
        Clean up after each test case by quitting the WebDriver instance.
        """
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
