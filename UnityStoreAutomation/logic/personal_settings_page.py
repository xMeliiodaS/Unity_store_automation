import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.base_app_page import BaseAppPage
from infra.logging_setup import logger_setup


class PersonalSettingsPage(BaseAppPage):
    EDIT_BIO = '//a[text() = "Edit Bio"]'
    EDIT_BIO_TEXTAREA_INPUT = '//textarea'
    SAVE_BIO_BUTTON = '//button[@label="Save"]'
    CURRENT_BIO_TEXT = '//div[@class="bQU15 e-vlo"]'

    def __init__(self, driver):
        """
        Initialize the LoginPage with a WebDriver instance.

        :param driver: The WebDriver instance to use for browser interactions.
        """
        super().__init__(driver)

    def click_on_edit_bio_button(self):
        """
        Clicks on the 'Edit Bio' button.

        This method waits for the 'Edit Bio' button to be present and then clicks on it.
        """
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.EDIT_BIO))).click()
        logging.info("Clicked on the Edit Bio button")

    def fill_bio_input(self, bio_text):
        """
        Fills in the bio input field with the provided text.

        This method waits for the bio input field to be present, clears any existing text,
        and then inputs the provided bio text.

        :param bio_text: The text to be entered into the bio input field.
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            self.EDIT_BIO_TEXTAREA_INPUT)))
        time.sleep(1)
        element.clear()
        element.send_keys(bio_text)
        logging.info("Filled the bio input")

    def click_on_save_bio_button(self):
        """
        Clicks on the 'Save Bio' button.

        This method waits for the 'Save Bio' button to be present and then clicks on it.
        """
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SAVE_BIO_BUTTON))).click()
        logging.info("Clicked on the 'Save Bio' button after changing the bio text")

    def edit_bio_flow(self, bio_text):
        """
        Performs the flow to edit the bio:
        1. Clicks on the 'Edit Bio' button.
        2. Fills in the bio input field with the provided text.
        3. Clicks on the 'Save Bio' button.

        :param bio_text: The text to be entered into the bio input field.
        """
        self.fill_bio_input(bio_text)
        self.click_on_save_bio_button()

    def get_current_bio_text(self):
        """
        Retrieves the current bio text.

        This method waits for the current bio text element to be present
        and then returns its text content.

        :return: The current bio text as a string.
        """
        self.refresh_page()
        return WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.CURRENT_BIO_TEXT))).text
