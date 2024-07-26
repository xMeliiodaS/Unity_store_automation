import logging
import unittest
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.jira_handler import JiraHandler
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
        logging.info("------------------------------SETUP------------------------------")

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

        self.jira_handler = JiraHandler()  # Initialize JiraHandler

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

        logging.info("--------------------------TEST COMPLETED---------------------------\n\n")


    def test_edit_bio_with_exceeding_char_limit(self):
        """
        Test editing the bio with invalid data (e.g., exceeding character limit).
        """
        logging.info("----------TESTING edit bio with exceeding character limit STARTED----------")
        logging.info(f"Logged in with email: {self.config['email']}")

        try:
            # Act
            text_to_insert = self.config["bio_text"]
            self.personal_settings_page.edit_bio_flow(text_to_insert)

            # Assert
            self.assertNotEqual(text_to_insert, self.personal_settings_page.get_current_bio_text())
            logging.info("--------------------------TEST COMPLETED---------------------------\n\n")

        except AssertionError as e:
            # Create a Jira issue if the assertion fails
            issue_summary = f"Assertion failed in test: {self.id()}"
            issue_description = f"Test case {self.id()} failed with assertion error: {str(e)}"
            self.jira_handler.create_issue(
                project_key="AT",  # Adjust the project key as necessary
                summary=issue_summary,
                description=issue_description,
                issue_type="Bug"
            )
            raise

        logging.info("--------------------------TEST COMPLETED---------------------------\n\n")

    def tearDown(self):
        """
        Clean up after each test case by quitting the WebDriver instance.
        """
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
