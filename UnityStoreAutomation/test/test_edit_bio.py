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
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])

        self.login_page = LoginPage(self.driver)
        self.login_page.login_flow(self.config["email"], self.config["password"])

        self.home_page = HomePage(self.driver)
        self.home_page.click_on_account_button()
        self.home_page.click_on_personal_settings_button()

        self.personal_settings_page = PersonalSettingsPage(self.driver)
        self.personal_settings_page.click_on_edit_bio_button()

    def test_edit_bio_successful(self):
        """
        Test the login functionality with valid credentials.
        """
        logging.info("----------TESTING edit bio functionality STARTED----------")
        logging.info(f"Logged in with email: {self.config['email']}")

        # Act
        text_to_insert = self.config["bio_text"]
        self.personal_settings_page.edit_bio_flow(text_to_insert)

        # Assert
        self.assertEqual(text_to_insert, self.personal_settings_page.get_current_bio_text())

        logging.info("---------------TEST COMPLETED---------------\n")

    def test_edit_bio_with_exceeding_char_limit(self):
        """
        Test editing the bio with invalid data (e.g., exceeding character limit).
        """
        logging.info("----------TESTING edit bio with exceeding character limit STARTED----------")
        logging.info(f"Logged in with email: {self.config['email']}")

        # Act
        self.personal_settings_page.edit_bio_flow(self.config["bio_text_exceeding_limit"] * 201)

        # Assert
        self.assertLessEqual(len(self.personal_settings_page.get_current_bio_text()),
                             self.config["Exceeding_char_limit"])

        logging.info("---------------TEST COMPLETED---------------\n")

    def tearDown(self):
        """
        Clean up after each test case by quitting the WebDriver instance.
        """
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
